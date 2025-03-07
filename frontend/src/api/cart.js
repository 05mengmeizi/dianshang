import request from './request'

// 获取购物车列表
export const getCartItems = () => {
  return request({
    url: '/cart/items',
    method: 'get'
  })
}

// 添加商品到购物车
export const addToCart = (productId, quantity = 1) => {
  return request({
    url: '/cart/items',
    method: 'post',
    data: {
      product_id: productId,
      quantity
    }
  })
}

// 更新购物车商品数量
export const updateCartItem = (productId, quantity) => {
  return request({
    url: `cart/items/${productId}`,
    method: 'put',
    data: {
      quantity
    }
  })
}

// 从购物车删除商品
export const removeFromCart = (productId) => {
  return request({
    url: `/cart/items/${productId}`,
    method: 'delete'
  })
}

// 清空购物车
export const clearCart = () => {
  return request({
    url: '/cart/items',
    method: 'delete'
  })
} 