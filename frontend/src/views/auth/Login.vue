<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-banner">
        <div class="banner-content">
          <h2>欢迎回来</h2>
          <p>登录您的账号，开启专属购物体验</p>
          <img 
            src="/login-illustration.svg" 
            alt="Login" 
            class="banner-image"
          >
        </div>
      </div>
      
      <div class="login-form">
        <div class="form-header">
          <h2>用户登录</h2>
          <p>还没有账号？<router-link to="/register">立即注册</router-link></p>
        </div>

        <el-form 
          :model="loginForm" 
          :rules="rules" 
          ref="loginFormRef"
          class="form-content"
        >
          <el-form-item prop="phone">
            <el-input
              v-model="loginForm.phone"
              placeholder="请输入手机号"
              size="large"
              :prefix-icon="Phone"
            />
          </el-form-item>
          
          <el-form-item prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              placeholder="请输入密码"
              size="large"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>

          <div class="form-options">
            <el-checkbox v-model="rememberMe">记住我</el-checkbox>
            <router-link to="/forgot-password" class="forgot-link">忘记密码？</router-link>
          </div>

          <el-button
            type="primary"
            :loading="loading"
            @click="handleLogin"
            size="large"
            class="submit-btn"
          >
            登录
          </el-button>

          <div class="divider">
            <span>或使用以下方式登录</span>
          </div>

          <div class="social-login">
            <el-button class="social-btn wechat">
              <el-icon><svg-icon name="wechat" /></el-icon>
              微信登录
            </el-button>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'
import { Phone, Lock } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const loginForm = ref({
  phone: '',
  password: ''
})

const loading = ref(false)
const loginFormRef = ref(null)
const rememberMe = ref(false)

const rules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
  ]
}

const handleLogin = async () => {
  if (!loginFormRef.value) return
  
  await loginFormRef.value.validate(async (valid) => {
    if (valid) {
      loading.value = true
      try {
        await userStore.login(loginForm.value.phone, loginForm.value.password)
        ElMessage.success('登录成功')
        const redirect = route.query.redirect || '/'
        router.push(redirect)
      } catch (error) {
        console.error('登录失败:', error)
      } finally {
        loading.value = false
      }
    }
  })
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e7eb 100%);
  padding: 20px;
}

.login-box {
  display: flex;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 1000px;
  max-width: 100%;
  min-height: 600px;
}

.login-banner {
  flex: 1;
  background: linear-gradient(135deg, #1890ff 0%, #0050b3 100%);
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.banner-content {
  text-align: center;
}

.banner-content h2 {
  font-size: 36px;
  margin-bottom: 16px;
}

.banner-content p {
  font-size: 16px;
  opacity: 0.9;
  margin-bottom: 40px;
}

.banner-image {
  width: 80%;
  max-width: 400px;
}

.login-form {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
}

.form-header {
  text-align: center;
  margin-bottom: 40px;
}

.form-header h2 {
  font-size: 28px;
  color: #303133;
  margin-bottom: 8px;
}

.form-header p {
  color: #909399;
}

.form-header a {
  color: var(--el-color-primary);
  text-decoration: none;
}

.form-content {
  max-width: 360px;
  margin: 0 auto;
  width: 100%;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.forgot-link {
  color: var(--el-color-primary);
  text-decoration: none;
  font-size: 14px;
}

.submit-btn {
  width: 100%;
  height: 44px;
  font-size: 16px;
}

.divider {
  display: flex;
  align-items: center;
  margin: 24px 0;
  color: #909399;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #dcdfe6;
}

.divider span {
  padding: 0 16px;
  font-size: 14px;
}

.social-login {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.social-btn {
  width: 100%;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.social-btn.wechat {
  background: #07c160;
  color: white;
}

.social-btn.wechat:hover {
  background: #06ad55;
}

@media (max-width: 768px) {
  .login-box {
    flex-direction: column;
  }

  .login-banner {
    padding: 30px;
  }

  .banner-content h2 {
    font-size: 28px;
  }

  .login-form {
    padding: 30px;
  }
}
</style> 