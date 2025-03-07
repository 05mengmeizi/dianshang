import request from './request'

export function login(phone, password) {
  return request({
    url: '/users/login/',
    method: 'post',
    data: { phone, password }
  })
}

export function register(userData) {
  return request({
    url: '/users/register/',
    method: 'post',
    data: userData
  })
}

export function logout() {
  return request({
    url: '/users/logout/',
    method: 'post'
  })
}

export function checkLoginStatus() {
  return request({
    url: '/users/check-login/',
    method: 'get'
  })
}

export function getUserInfo() {
  return request({
    url: '/users/info/',
    method: 'get'
  })
} 