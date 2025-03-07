import request from './request'

// 获取商品列表
export function getProducts(params) {
  return request({
    url: '/products/',
    method: 'get',
    params
  })
}

// 获取商品分类
export function getCategories() {
  return request({
    url: '/products/categories/',
    method: 'get'
  })
}

// 获取商品详情
export function getProductDetail(id) {
  return request({
    url: `/products/${id}/`,
    method: 'get'
  })
}

// 获取推荐商品
export function getFeaturedProducts() {
  return request({
    url: '/products/featured/',
    method: 'get'
  })
}

// 获取商品评价
export function getProductReviews(productId, params) {
  return request({
    url: `/products/${productId}/reviews/`,
    method: 'get',
    params
  })
} 