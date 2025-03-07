import { defineStore } from 'pinia'
import { ref } from 'vue'
import { login as loginApi, logout as logoutApi, checkLoginStatus, register as registerApi } from '@/api/users'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const isLoggedIn = ref(false)

  async function login(phone, password) {
    try {
      const response = await loginApi(phone, password)
      user.value = response.data.user
      isLoggedIn.value = true
      return response
    } catch (error) {
      throw error
    }
  }

  async function register(userData) {
    try {
      const response = await registerApi(userData)
      user.value = response.data.user
      isLoggedIn.value = true
      return response
    } catch (error) {
      throw error
    }
  }

  async function logout() {
    try {
      await logoutApi()
      clearUserInfo()
    } catch (error) {
      throw error
    }
  }

  async function checkAuth() {
    try {
      const response = await checkLoginStatus()
      if (response.data.isLoggedIn) {
        user.value = response.data.user
        isLoggedIn.value = true
      } else {
        clearUserInfo()
      }
      return response.data.isLoggedIn
    } catch (error) {
      clearUserInfo()
      return false
    }
  }

  function clearUserInfo() {
    user.value = null
    isLoggedIn.value = false
  }

  return {
    user,
    isLoggedIn,
    login,
    register,
    logout,
    checkAuth,
    clearUserInfo
  }
}) 