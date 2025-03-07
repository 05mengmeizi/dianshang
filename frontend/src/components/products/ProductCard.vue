<template>
  <el-card 
    class="product-card" 
    :body-style="{ padding: '0px' }"
    @click="handleViewDetail"
  >
    <div class="product-image">
      <img :src="defaultImage" :alt="product.name">
    </div>
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <div class="product-price">
        <span class="price">¥{{ formatPrice(product.price) }}</span>
      </div>
      <p class="product-description">{{ product.description || '暂无描述' }}</p>
      <div class="product-meta">
        <span class="stock-info">库存: {{ product.stock || 0 }}</span>
      </div>
      <div class="product-actions" @click.stop>
        <el-button 
          type="success" 
          size="small" 
          @click="handleAddToCart"
          :loading="cartStore.isLoading"
        >
          <el-icon><ShoppingCart /></el-icon>
          加入购物车
        </el-button>
      </div>
    </div>
  </el-card>
</template>

<script setup>
import { computed } from 'vue'
import { ShoppingCart } from '@element-plus/icons-vue'
import { useCartStore } from '@/stores/cart'
import { useUserStore } from '@/stores/user'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['view-detail', 'add-to-cart'])

const cartStore = useCartStore()
const userStore = useUserStore()

// 使用示例图片占位符
const defaultImage = computed(() => {
  return `https://placehold.co/400x300/f1f5f9/64748b?text=${encodeURIComponent(props.product.name)}`
})

const formatPrice = (price) => {
  if (price === null || price === undefined) {
    return '0.00'
  }
  const numPrice = Number(price)
  return isNaN(numPrice) ? '0.00' : numPrice.toFixed(2)
}

const handleViewDetail = () => {
  emit('view-detail', props.product.id)
}

const handleAddToCart = () => {
  emit('add-to-cart', props.product)
}
</script>

<style scoped>
.product-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
  cursor: pointer;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image {
  height: 200px;
  overflow: hidden;
  background-color: #f1f5f9;
  border-radius: 4px 4px 0 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.3s ease;
}

.product-image img:hover {
  opacity: 0.9;
}

.product-info {
  padding: 14px;
}

.product-name {
  margin: 0;
  font-size: 16px;
  font-weight: bold;
  color: #334155;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.product-price {
  margin: 10px 0;
}

.price {
  color: #f56c6c;
  font-size: 18px;
  font-weight: bold;
}

.product-description {
  font-size: 14px;
  color: #666;
  margin: 10px 0;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.product-meta {
  margin-top: 10px;
}

.stock-info {
  color: #409EFF;
  font-size: 14px;
}

.product-actions {
  margin-top: 15px;
  text-align: center;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.el-button-group {
  display: flex;
  gap: 8px;
}

:deep(.el-button) {
  flex: 1;
}

:deep(.el-icon) {
  margin-right: 4px;
}
</style> 