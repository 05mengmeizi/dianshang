import request from './request'

export function register(data) {
  return request({
    url: '/users/register/',
    method: 'post',
    data
  })
}

export function login(data) {
  return request({
    url: '/users/login/',
    method: 'post',
    data
  })
}

export function getUserInfo() {
  return request({
    url: '/users/info/',
    method: 'get'
  })
} 