import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { getCartItems, addToCart, updateCartItem, removeFromCart, clearCart as clearCartApi } from '@/api/cart'

export const useCartStore = defineStore('cart', () => {
  const cartItems = ref([])
  const loading = ref(false)
  
  // 计算总数量
  const totalCount = computed(() => {
    return cartItems.value.reduce((total, item) => total + item.quantity, 0)
  })
  
  // 计算总价格
  const totalPrice = computed(() => {
    return cartItems.value.reduce((total, item) => total + item.product.price * item.quantity, 0)
  })

  // 从后端获取购物车数据
  const fetchCartItems = async () => {
    try {
      loading.value = true
      const { data } = await getCartItems()
      cartItems.value = data
    } catch (error) {
      console.error('获取购物车数据失败:', error)
      ElMessage.error('获取购物车数据失败')
    } finally {
      loading.value = false
    }
  }
  
  // 添加商品到购物车
  const addToCartAction = async (product) => {
    try {
      loading.value = true
      await addToCart(product.id)
      await fetchCartItems() // 重新获取最新的购物车数据
      ElMessage.success('商品已添加到购物车')
    } catch (error) {
      console.error('添加到购物车失败:', error)
      ElMessage.error('添加到购物车失败')
    } finally {
      loading.value = false
    }
  }
  
  // 更新商品数量
  const updateQuantity = async (productId, quantity) => {
    try {
      loading.value = true
      await updateCartItem(productId, quantity)
      await fetchCartItems() // 重新获取最新的购物车数据
      ElMessage.success('商品数量已更新')
    } catch (error) {
      console.error('更新商品数量失败:', error)
      ElMessage.error('更新商品数量失败')
    } finally {
      loading.value = false
    }
  }
  
  // 从购物车移除商品
  const removeFromCartAction = async (productId) => {
    try {
      loading.value = true
      await removeFromCart(productId)
      await fetchCartItems() // 重新获取最新的购物车数据
      ElMessage.success('商品已从购物车移除')
    } catch (error) {
      console.error('移除商品失败:', error)
      ElMessage.error('移除商品失败')
    } finally {
      loading.value = false
    }
  }
  
  // 清空购物车
  const clearCart = async () => {
    try {
      loading.value = true
      await clearCartApi()
      cartItems.value = []
      ElMessage.success('购物车已清空')
    } catch (error) {
      console.error('清空购物车失败:', error)
      ElMessage.error('清空购物车失败')
    } finally {
      loading.value = false
    }
  }

  return {
    cartItems,
    loading,
    totalCount,
    totalPrice,
    fetchCartItems,
    addToCart: addToCartAction,
    updateQuantity,
    removeFromCart: removeFromCartAction,
    clearCart
  }
}) 