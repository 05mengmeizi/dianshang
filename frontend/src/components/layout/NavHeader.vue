<template>
  <div class="nav-header">
    <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      router
    >
      <div class="logo">
        <router-link to="/">"头雁"农产品交易平台</router-link>
      </div>
      
      <div class="menu-items">
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/products">商品列表</el-menu-item>
        
        <!-- 未登录状态 -->
        <template v-if="!userStore.isLoggedIn">
          <el-menu-item index="/login">登录</el-menu-item>
          <el-menu-item index="/register">注册</el-menu-item>
        </template>
        
        <!-- 登录状态 -->
        <template v-else>
          <el-menu-item index="/cart">
            <el-badge :value="cartStore.totalCount" class="cart-badge">
              <el-icon><ShoppingCart /></el-icon> 购物车
            </el-badge>
          </el-menu-item>
          
          <el-sub-menu index="user">
            <template #title>
              <el-avatar 
                :size="32" 
                :src="userStore.user?.avatar || '/default-avatar.png'"
              />
              <span class="user-phone">{{ userStore.user?.phone }}</span>
            </template>
            <el-menu-item index="/orders">我的订单</el-menu-item>
            <el-menu-item index="/profile">个人信息</el-menu-item>
            <el-menu-item @click="handleLogout">退出登录</el-menu-item>
          </el-sub-menu>
        </template>
      </div>
    </el-menu>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useCartStore } from '@/stores/cart'
import { ElMessage, ElMessageBox } from 'element-plus'
import { ShoppingCart } from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const cartStore = useCartStore()

const activeIndex = computed(() => route.path)

// 在组件挂载时获取购物车数据
onMounted(() => {
  if (userStore.isLoggedIn) {
    cartStore.fetchCartItems()
  }
})

const handleLogout = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要退出登录吗？',
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    )
    
    await userStore.logout()
    ElMessage.success('已退出登录')
    router.push('/login')
  } catch (error) {
    if (error !== 'cancel') {
      console.error('退出登录失败:', error)
      ElMessage.error('退出登录失败')
    }
  }
}
</script>

<style scoped>
.nav-header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.el-menu {
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
}

.logo {
  display: flex;
  align-items: center;
  font-size: 24px;
  font-weight: bold;
}

.logo a {
  color: var(--el-color-primary);
  text-decoration: none;
}

.menu-items {
  display: flex;
  align-items: center;
}

.cart-badge :deep(.el-badge__content) {
  z-index: 1;
}

.user-phone {
  margin-left: 8px;
  font-size: 14px;
}

:deep(.el-sub-menu__title) {
  display: flex;
  align-items: center;
}
</style> 