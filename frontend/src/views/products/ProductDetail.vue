<template>
  <div class="product-detail" v-if="product">
    <el-row :gutter="40">
      <el-col :span="12">
        <div class="product-gallery">
          <el-image 
            :src="product.image" 
            :preview-src-list="[product.image]"
            fit="cover"
          />
        </div>
      </el-col>
      
      <el-col :span="12">
        <div class="product-info">
          <h1 class="product-name">{{ product.name }}</h1>
          
          <div class="product-price">
            <span class="price-label">价格：</span>
            <span class="price">¥{{ product.price }}</span>
          </div>
          
          <div class="product-stock">
            <span class="stock-label">库存：</span>
            <span class="stock">{{ product.stock }}件</span>
          </div>
          
          <div class="product-quantity">
            <span class="quantity-label">数量：</span>
            <el-input-number 
              v-model="quantity" 
              :min="1" 
              :max="product.stock"
            />
          </div>
          
          <div class="product-actions">
            <el-button 
              type="primary" 
              size="large" 
              @click="addToCart"
              :disabled="product.stock === 0"
            >
              加入购物车
            </el-button>
            <el-button 
              type="danger" 
              size="large" 
              @click="buyNow"
              :disabled="product.stock === 0"
            >
              立即购买
            </el-button>
          </div>
          
          <div class="product-description">
            <h3>商品描述</h3>
            <p>{{ product.description }}</p>
          </div>
        </div>
      </el-col>
    </el-row>

    <div class="product-reviews">
      <h2>商品评价</h2>
      <product-reviews :product-id="product.id" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { getProductDetail } from '@/api/products'
import ProductReviews from '@/components/products/ProductReviews.vue'

const route = useRoute()
const router = useRouter()
const product = ref(null)
const quantity = ref(1)

onMounted(async () => {
  try {
    const response = await getProductDetail(route.params.id)
    product.value = response.data
  } catch (error) {
    ElMessage.error('获取商品详情失败')
  }
})

const addToCart = async () => {
  // 添加到购物车的逻辑
  ElMessage.success('已添加到购物车')
}

const buyNow = () => {
  // 立即购买的逻辑
  router.push({
    path: '/checkout',
    query: {
      products: JSON.stringify([{
        id: product.value.id,
        quantity: quantity.value
      }])
    }
  })
}
</script>

<style scoped>
.product-detail {
  padding: 20px;
  background: #fff;
  border-radius: 4px;
}

.product-gallery {
  border: 1px solid #eee;
  padding: 10px;
}

.product-info {
  padding: 20px;
}

.product-name {
  margin: 0 0 20px;
  font-size: 24px;
}

.product-price {
  margin: 20px 0;
}

.price {
  color: #f56c6c;
  font-size: 28px;
  font-weight: bold;
}

.product-stock,
.product-quantity {
  margin: 15px 0;
}

.product-actions {
  margin: 30px 0;
  display: flex;
  gap: 20px;
}

.product-description {
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

.product-reviews {
  margin-top: 40px;
}
</style> 