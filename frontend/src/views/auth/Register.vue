<template>
  <div class="register-container">
    <div class="register-box">
      <div class="register-banner">
        <div class="banner-content">
          <h2>加入我们</h2>
          <p>创建账号，享受专属购物体验</p>
          <img 
            src="/register-illustration.svg" 
            alt="Register" 
            class="banner-image"
          >
        </div>
      </div>
      
      <div class="register-form">
        <div class="form-header">
          <h2>用户注册</h2>
          <p>已有账号？<router-link to="/login">立即登录</router-link></p>
        </div>

        <el-form 
          :model="registerForm" 
          :rules="rules" 
          ref="registerFormRef"
          class="form-content"
        >
          <el-form-item prop="phone">
            <el-input
              v-model="registerForm.phone"
              placeholder="请输入手机号"
              size="large"
              :prefix-icon="Phone"
            />
          </el-form-item>
          
          <el-form-item prop="password">
            <el-input
              v-model="registerForm.password"
              type="password"
              placeholder="请设置密码"
              size="large"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>

          <el-form-item prop="confirmPassword">
            <el-input
              v-model="registerForm.confirmPassword"
              type="password"
              placeholder="请确认密码"
              size="large"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>

          <el-form-item class="agreement">
            <el-checkbox v-model="agreeTerms">
              我已阅读并同意
              <el-link type="primary" @click="showTerms">用户协议</el-link>
              和
              <el-link type="primary" @click="showPrivacy">隐私政策</el-link>
            </el-checkbox>
          </el-form-item>

          <el-button
            type="primary"
            :loading="loading"
            @click="handleRegister"
            size="large"
            class="submit-btn"
            :disabled="!agreeTerms"
          >
            注册
          </el-button>

          <div class="divider">
            <span>或使用以下方式注册</span>
          </div>

          <div class="social-login">
            <el-button class="social-btn wechat">
              <el-icon><svg-icon name="wechat" /></el-icon>
              微信注册
            </el-button>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'
import { Phone, Lock } from '@element-plus/icons-vue'

const router = useRouter()
const userStore = useUserStore()

const registerForm = ref({
  phone: '',
  password: '',
  confirmPassword: ''
})

const loading = ref(false)
const registerFormRef = ref(null)
const agreeTerms = ref(false)

const validatePass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    if (registerForm.value.confirmPassword !== '') {
      registerFormRef.value.validateField('confirmPassword')
    }
    callback()
  }
}

const validatePass2 = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请再次输入密码'))
  } else if (value !== registerForm.value.password) {
    callback(new Error('两次输入密码不一致!'))
  } else {
    callback()
  }
}

const rules = {
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  password: [
    { required: true, validator: validatePass, trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, validator: validatePass2, trigger: 'blur' }
  ]
}

const showTerms = () => {
  // 显示用户协议
}

const showPrivacy = () => {
  // 显示隐私政策
}

const handleRegister = async () => {
  if (!registerFormRef.value) return
  
  await registerFormRef.value.validate(async (valid) => {
    if (valid) {
      if (!agreeTerms.value) {
        ElMessage.warning('请先同意用户协议和隐私政策')
        return
      }
      
      loading.value = true
      try {
        const { confirmPassword, ...userData } = registerForm.value
        await userStore.register(userData)
        ElMessage.success('注册成功')
        router.push('/')
      } catch (error) {
        console.error('注册失败:', error)
      } finally {
        loading.value = false
      }
    }
  })
}
</script>

<style scoped>
/* 复用登录页面的基础样式 */
.register-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e7eb 100%);
  padding: 20px;
}

.register-box {
  display: flex;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 1000px;
  max-width: 100%;
  min-height: 700px;
}

.register-banner {
  flex: 1;
  background: linear-gradient(135deg, #722ed1 0%, #1890ff 100%);
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

/* 其他样式与登录页面相同，只需修改类名 */
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

.register-form {
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

.agreement {
  margin-bottom: 24px;
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
  .register-box {
    flex-direction: column;
  }

  .register-banner {
    padding: 30px;
  }

  .banner-content h2 {
    font-size: 28px;
  }

  .register-form {
    padding: 30px;
  }
}
</style> 