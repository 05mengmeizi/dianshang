import request from './request'

export function getOrders() {
  return request({
    url: '/orders/',
    method: 'get'
  })
}

export function getOrderDetail(id) {
  return request({
    url: `/orders/${id}/`,
    method: 'get'
  })
}

export function createOrder(data) {
  return request({
    url: '/orders/',
    method: 'post',
    data
  })
} 