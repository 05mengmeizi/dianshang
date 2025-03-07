<template>
  <div class="cart-container">
    <el-card class="cart-card" v-loading="cartStore.loading">
      <template #header>
        <div class="cart-header">
          <h2>我的购物车</h2>
          <el-button 
            type="danger" 
            plain 
            size="small" 
            @click="handleClearCart"
            :disabled="!cartStore.cartItems.length"
          >
            清空购物车
          </el-button>
        </div>
      </template>

      <!-- 空购物车状态 -->
      <el-empty
        v-if="!cartStore.cartItems.length"
        description="购物车是空的"
      >
        <el-button type="primary" @click="$router.push('/products')">
          去购物
        </el-button>
      </el-empty>

      <!-- 购物车商品列表 -->
      <div v-else class="cart-items">
        <el-table :data="cartStore.cartItems" style="width: 100%">
          <el-table-column label="商品" width="400">
            <template #default="{ row }">
              <div class="product-info">
                <el-image
                  :src="row.product.image"
                  fit="cover"
                  class="product-image"
                  @click="$router.push(`/products/${row.product.id}`)"
                />
                <span class="product-name">{{ row.product.name }}</span>
              </div>
            </template>
          </el-table-column>

          <el-table-column label="单价" width="120">
            <template #default="{ row }">
              ¥{{ row.product.price.toFixed(2) }}
            </template>
          </el-table-column>

          <el-table-column label="数量" width="200">
            <template #default="{ row }">
              <el-input-number
                v-model="row.quantity"
                :min="1"
                :max="99"
                @change="(value) => handleQuantityChange(row.product.id, value)"
              />
            </template>
          </el-table-column>

          <el-table-column label="小计" width="120">
            <template #default="{ row }">
              ¥{{ (row.product.price * row.quantity).toFixed(2) }}
            </template>
          </el-table-column>

          <el-table-column label="操作">
            <template #default="{ row }">
              <el-button
                type="danger"
                link
                @click="handleRemoveItem(row.product.id)"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>

        <!-- 购物车底部 -->
        <div class="cart-footer">
          <div class="cart-total">
            <span>共 {{ cartStore.totalCount }} 件商品</span>
            <span class="total-price">
              合计：<strong>¥{{ cartStore.totalPrice.toFixed(2) }}</strong>
            </span>
          </div>
          <el-button type="primary" size="large" @click="handleCheckout">
            结算
          </el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCartStore } from '@/stores/cart'
import { ElMessageBox } from 'element-plus'

const cartStore = useCartStore()

// 初始化获取购物车数据
onMounted(() => {
  cartStore.fetchCartItems()
})

// 更新商品数量
const handleQuantityChange = (productId, quantity) => {
  cartStore.updateQuantity(productId, quantity)
}

// 移除商品
const handleRemoveItem = async (productId) => {
  try {
    await ElMessageBox.confirm(
      '确定要从购物车中移除该商品吗？',
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    )
    cartStore.removeFromCart(productId)
  } catch (error) {
    // 用户取消操作
  }
}

// 清空购物车
const handleClearCart = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要清空购物车吗？',
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    )
    cartStore.clearCart()
  } catch (error) {
    // 用户取消操作
  }
}

// 结算
const handleCheckout = () => {
  // TODO: 实现结算功能
  ElMessageBox.alert('结算功能开发中...', '提示')
}
</script>

<style scoped>
.cart-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 0 20px;
}

.cart-card {
  margin-bottom: 20px;
}

.cart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-header h2 {
  margin: 0;
  font-size: 20px;
}

.product-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.product-image {
  width: 80px;
  height: 80px;
  border-radius: 4px;
  cursor: pointer;
}

.product-name {
  font-size: 14px;
}

.cart-footer {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 24px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #ebeef5;
}

.cart-total {
  display: flex;
  align-items: center;
  gap: 16px;
}

.total-price {
  font-size: 16px;
}

.total-price strong {
  color: #f56c6c;
  font-size: 20px;
}
</style> 