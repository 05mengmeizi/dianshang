<template>
  <div class="home">
    <!-- 顶部横幅区域 -->
    <div class="banner-section">
      <el-carousel height="400px">
        <el-carousel-item v-for="(banner, index) in banners" :key="index">
          <div class="banner-content" :style="{ backgroundImage: `url(${banner.image})` }">
            <div class="banner-text">
              <h1>{{ banner.title }}</h1>
              <p>{{ banner.description }}</p>
              <el-button type="primary" size="large" @click="handleBannerAction(banner)">
                {{ banner.buttonText }}
              </el-button>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>

    <!-- 欢迎区域 -->
    <div class="content-section">
      <el-row :gutter="20">
        <!-- 已登录状态 -->
        <template v-if="userStore.isLoggedIn">
          <el-col :span="24">
            <el-card class="welcome-card">
              <div class="user-welcome">
                <div class="welcome-header">
                  <el-avatar 
                    :size="64" 
                    :src="userStore.user?.avatar || '/default-avatar.png'"
                  />
                  <div class="welcome-text">
                    <h2>欢迎回来，{{ userStore.user?.phone }}</h2>
                    <p>今天为您精选了一些商品</p>
                  </div>
                </div>
                <div class="quick-actions">
                  <el-button-group>
                    <el-button type="primary" @click="router.push('/products')">
                      <el-icon><Shop /></el-icon> 浏览商品
                    </el-button>
                    <el-button type="success" @click="router.push('/cart')">
                      <el-icon><ShoppingCart /></el-icon> 购物车
                    </el-button>
                    <el-button type="info" @click="router.push('/orders')">
                      <el-icon><List /></el-icon> 我的订单
                    </el-button>
                  </el-button-group>
                </div>
              </div>
            </el-card>
          </el-col>
        </template>

        <!-- 未登录状态 -->
        <template v-else>
          <el-col :span="24">
            <el-card class="welcome-card">
              <div class="guest-welcome">
                <div class="welcome-content">
                  <h2>欢迎来到我们的电商平台</h2>
                  <p>立即登录，开启您的专属购物之旅</p>
                  <div class="auth-buttons">
                    <el-button type="primary" size="large" @click="router.push('/login')">
                      <el-icon><Key /></el-icon> 登录账号
                    </el-button>
                    <el-button size="large" @click="router.push('/register')">
                      <el-icon><User /></el-icon> 注册账号
                    </el-button>
                  </div>
                </div>
                <div class="benefits">
                  <div class="benefit-item" v-for="(benefit, index) in benefits" :key="index">
                    <el-icon :size="32" :color="benefit.color">
                      <component :is="benefit.icon" />
                    </el-icon>
                    <h3>{{ benefit.title }}</h3>
                    <p>{{ benefit.description }}</p>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
        </template>
      </el-row>

      <!-- 热门商品区域 -->
      <div class="featured-section">
        <div class="section-header">
          <h2>热门商品推荐</h2>
          <el-button text @click="router.push('/products')">
            查看更多 <el-icon><ArrowRight /></el-icon>
          </el-button>
        </div>
        
        <el-row :gutter="20">
          <el-col 
            :xs="24" :sm="12" :md="8" :lg="6"
            v-for="product in featuredProducts" 
            :key="product.id"
          >
            <product-card :product="product" />
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { getFeaturedProducts } from '@/api/products'
import ProductCard from '@/components/products/ProductCard.vue'
import { 
  Shop, ShoppingCart, List, Key, User, 
  GoodsFilled, PriceTag, TrophyBase, Service,
  ArrowRight
} from '@element-plus/icons-vue'

const router = useRouter()
const userStore = useUserStore()
const featuredProducts = ref([])

// 轮播图数据
const banners = [
  {
    image: '/banner1.jpg',
    title: '新品上市',
    description: '发现最新潮流商品',
    buttonText: '立即查看',
    action: '/products'
  },
  {
    image: '/banner2.jpg',
    title: '限时特惠',
    description: '精选商品低至5折',
    buttonText: '马上抢购',
    action: '/products?sort=price_asc'
  },
  // 可以添加更多轮播图
]

// 未登录状态下显示的权益
const benefits = [
  {
    icon: 'GoodsFilled',
    title: '正品保障',
    description: '品质保证，假一赔十',
    color: '#409EFF'
  },
  {
    icon: 'PriceTag',
    title: '优惠福利',
    description: '会员专享优惠券',
    color: '#67C23A'
  },
  {
    icon: 'TrophyBase',
    title: '积分奖励',
    description: '购物即可获得积分',
    color: '#E6A23C'
  },
  {
    icon: 'Service',
    title: '贴心服务',
    description: '7×24小时客服支持',
    color: '#F56C6C'
  }
]

const handleBannerAction = (banner) => {
  router.push(banner.action)
}

const loadFeaturedProducts = async () => {
  try {
    const response = await getFeaturedProducts()
    featuredProducts.value = response.data
  } catch (error) {
    console.error('获取推荐商品失败:', error)
  }
}

onMounted(() => {
  loadFeaturedProducts()
})
</script>

<style scoped>
.home {
  min-height: 100vh;
  background-color: #f5f7fa;
}

.banner-section {
  margin-bottom: 30px;
}

.banner-content {
  height: 100%;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  padding: 0 10%;
}

.banner-text {
  color: white;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.banner-text h1 {
  font-size: 48px;
  margin-bottom: 20px;
}

.banner-text p {
  font-size: 24px;
  margin-bottom: 30px;
}

.content-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.welcome-card {
  margin-bottom: 30px;
  border-radius: 8px;
  overflow: hidden;
}

.user-welcome {
  padding: 20px;
}

.welcome-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.welcome-text {
  margin-left: 20px;
}

.welcome-text h2 {
  margin: 0;
  font-size: 24px;
  color: #303133;
}

.welcome-text p {
  margin: 8px 0 0;
  color: #909399;
}

.quick-actions {
  display: flex;
  justify-content: center;
}

.guest-welcome {
  padding: 40px;
  text-align: center;
}

.welcome-content h2 {
  font-size: 32px;
  color: #303133;
  margin-bottom: 16px;
}

.welcome-content p {
  font-size: 16px;
  color: #606266;
  margin-bottom: 24px;
}

.auth-buttons {
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
  gap: 16px;
}

.benefits {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 40px;
}

.benefit-item {
  text-align: center;
  padding: 20px;
}

.benefit-item h3 {
  margin: 16px 0 8px;
  color: #303133;
}

.benefit-item p {
  color: #909399;
  font-size: 14px;
}

.featured-section {
  margin-top: 40px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h2 {
  font-size: 24px;
  color: #303133;
  margin: 0;
}

@media (max-width: 768px) {
  .benefits {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .banner-text h1 {
    font-size: 32px;
  }
  
  .banner-text p {
    font-size: 18px;
  }
}

@media (max-width: 480px) {
  .benefits {
    grid-template-columns: 1fr;
  }
  
  .auth-buttons {
    flex-direction: column;
  }
}
</style> 