<template>
  <el-container class="layout-container">
    <el-header>
      <nav-header />
    </el-header>
    
    <el-main>
      <router-view v-slot="{ Component }">
        <keep-alive>
          <component :is="Component" :key="$route.fullPath" />
        </keep-alive>
      </router-view>
    </el-main>
    
    <el-footer>
      <nav-footer />
    </el-footer>
  </el-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import NavHeader from '@/components/layout/NavHeader.vue'
import NavFooter from '@/components/layout/NavFooter.vue'

const userStore = useUserStore()

onMounted(async () => {
  await userStore.checkAuth()
})
</script>

<style>
@import 'element-plus/dist/index.css';

.layout-container {
  min-height: 100vh;
}

.el-header {
  padding: 0;
  height: 60px;
}

.el-main {
  padding: 20px;
  background-color: #f5f5f5;
}

.el-footer {
  padding: 0;
}
</style> 