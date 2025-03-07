<template>
  <div class="product-list">
    <el-row :gutter="20">
      <el-col :span="4">
        <div class="filter-section">
          <h3>商品分类</h3>
          <el-card class="category-list">
            <el-menu
              :default-active="selectedCategory"
              @select="handleCategorySelect"
              class="category-menu"
            >
              <el-menu-item index="">
                <el-icon><Grid /></el-icon>
                <span>全部商品</span>
              </el-menu-item>
              <el-menu-item 
                v-for="category in categories" 
                :key="category.id"
                :index="category.id.toString()"
              >
                <el-icon><Folder /></el-icon>
                <span>{{ category.name }}</span>
              </el-menu-item>
            </el-menu>
          </el-card>

          <h3>价格区间</h3>
          <el-slider
            v-model="priceRange"
            range
            :min="0"
            :max="10000"
            @change="handlePriceChange"
          />
        </div>
      </el-col>

      <el-col :span="20">
        <div class="product-grid" v-loading="loading">
          <div class="toolbar">
            <el-input
              v-model="searchKeyword"
              placeholder="搜索商品"
              class="search-input"
              @input="handleSearch"
            >
              <template #prefix>
                <el-icon><Search /></el-icon>
              </template>
            </el-input>
            
            <el-select v-model="sortBy" @change="handleSort">
              <el-option label="默认排序" value="" />
              <el-option label="价格从低到高" value="price_asc" />
              <el-option label="价格从高到低" value="price_desc" />
              <el-option label="最新上架" value="newest" />
            </el-select>
          </div>

          <div v-if="products.length === 0 && !loading" class="no-data">
            <p>暂无商品数据</p>
            <p>Debug info:</p>
            <pre>{{ { products: products.length, loading, selectedCategory } }}</pre>
          </div>

          <el-row :gutter="20" v-else>
            <el-col 
              :xs="24" 
              :sm="12" 
              :md="8" 
              :lg="6"
              v-for="product in products" 
              :key="product.id"
            >
              <product-card 
                :product="product"
                @view-detail="viewDetail"
                @add-to-cart="addToCart"
              />
            </el-col>
          </el-row>

          <div class="pagination">
            <el-pagination
              v-model:current-page="currentPage"
              v-model:page-size="pageSize"
              :total="total"
              :page-sizes="[12, 24, 36, 48]"
              layout="total, sizes, prev, pager, next"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
            />
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Search, Grid, Folder, ShoppingCart } from '@element-plus/icons-vue'
import { getProducts, getCategories } from '@/api/products'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { useUserStore } from '@/stores/user'
import ProductCard from '@/components/products/ProductCard.vue'

const router = useRouter()
const cartStore = useCartStore()
const userStore = useUserStore()

const products = ref([])
const categories = ref([])
const loading = ref(false)
const selectedCategory = ref('')
const priceRange = ref([0, 10000])
const searchKeyword = ref('')
const sortBy = ref('')
const currentPage = ref(1)
const pageSize = ref(12)
const total = ref(0)

const fetchProducts = async () => {
  try {
    loading.value = true
    const params = {
      page: currentPage.value,
      page_size: pageSize.value,
      category: selectedCategory.value,
      min_price: priceRange.value[0],
      max_price: priceRange.value[1],
      search: searchKeyword.value,
      ordering: sortBy.value
    }
    console.log('Fetching products with params:', params)
    const response = await getProducts(params)
    console.log('Products response:', response)
    
    if (response && response.data) {
      if (response.data.results) {
        products.value = response.data.results
        total.value = response.data.count
      } else {
        products.value = Array.isArray(response.data) ? response.data : [response.data]
        total.value = products.value.length
      }
      console.log('Products loaded:', products.value)
    } else {
      products.value = []
      total.value = 0
      console.log('No products data in response')
    }

    if (products.value.length === 0) {
      ElMessage.info('暂无商品数据')
    }
  } catch (error) {
    console.error('获取商品列表失败:', error)
    ElMessage.error('获取商品列表失败')
    products.value = []
    total.value = 0
  } finally {
    loading.value = false
  }
}

const fetchCategories = async () => {
  try {
    const { data } = await getCategories()
    categories.value = data
  } catch (error) {
    console.error('获取分类列表失败:', error)
    ElMessage.error('获取分类列表失败')
  }
}

const handleCategorySelect = (categoryId) => {
  selectedCategory.value = categoryId
  currentPage.value = 1
  fetchProducts()
}

const handlePriceChange = () => {
  currentPage.value = 1
  fetchProducts()
}

const handleSearch = () => {
  currentPage.value = 1
  fetchProducts()
}

const handleSort = () => {
  fetchProducts()
}

const handleSizeChange = (val) => {
  pageSize.value = val
  fetchProducts()
}

const handleCurrentChange = (val) => {
  currentPage.value = val
  fetchProducts()
}

const getProductImage = (product) => {
  return `https://placehold.co/400x300/f1f5f9/64748b?text=${encodeURIComponent(product.name)}`
}

const getCategoryName = (categoryId) => {
  const category = categories.value.find(c => c.id === categoryId)
  return category ? category.name : '未分类'
}

const viewDetail = (productId) => {
  router.push(`/products/${productId}`)
}

const formatPrice = (price) => {
  if (price === null || price === undefined) {
    return '0.00'
  }
  // 确保price是数字
  const numPrice = Number(price)
  return isNaN(numPrice) ? '0.00' : numPrice.toFixed(2)
}

const addToCart = async (product) => {
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    router.push('/login')
    return
  }

  try {
    await cartStore.addToCart({
      product_id: product.id,
      quantity: 1
    })
    ElMessage.success('已添加到购物车')
  } catch (error) {
    console.error('添加到购物车失败:', error)
    ElMessage.error('添加到购物车失败')
  }
}

onMounted(() => {
  fetchCategories()
  fetchProducts()
})
</script>

<style scoped>
.product-list {
  padding: 20px;
}

.filter-section {
  background: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.filter-section h3 {
  margin-top: 0;
  margin-bottom: 15px;
  font-size: 16px;
  color: #333;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.category-list {
  border: none;
  box-shadow: none;
}

.category-menu {
  border-right: none;
}

:deep(.el-menu-item) {
  height: 40px;
  line-height: 40px;
  margin: 4px 0;
  border-radius: 4px;
}

:deep(.el-menu-item.is-active) {
  background-color: #ecf5ff;
  color: #409eff;
}

:deep(.el-menu-item:hover) {
  background-color: #f5f7fa;
}

.el-icon {
  margin-right: 8px;
  font-size: 16px;
}

.product-grid {
  background: #fff;
  padding: 20px;
  border-radius: 4px;
  min-height: 400px;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.search-input {
  width: 300px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.no-data {
  text-align: center;
  padding: 40px;
  color: #666;
}

.no-data pre {
  text-align: left;
  background: #f5f5f5;
  padding: 10px;
  border-radius: 4px;
  margin-top: 10px;
}

.product-detail-card,
.product-name,
.product-price,
.price,
.product-description,
.product-meta,
.stock-info,
.product-actions,
.el-button-group,
.product-image,
.product-image img {
  /* 这些样式已在 ProductCard 组件中定义 */
}
</style> 