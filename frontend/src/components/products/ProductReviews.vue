<template>
  <div class="product-reviews">
    <div class="reviews-header">
      <h3>用户评价 ({{ total }})</h3>
      <el-rate
        v-model="averageRating"
        disabled
        show-score
        text-color="#ff9900"
      />
    </div>

    <div class="reviews-list">
      <div v-for="review in reviews" :key="review.id" class="review-item">
        <div class="review-header">
          <div class="user-info">
            <el-avatar :size="32" :src="review.user.avatar" />
            <span class="username">{{ review.user.username }}</span>
          </div>
          <el-rate v-model="review.rating" disabled />
        </div>
        <div class="review-content">
          {{ review.content }}
        </div>
        <div class="review-images" v-if="review.images?.length">
          <el-image
            v-for="image in review.images"
            :key="image"
            :src="image"
            :preview-src-list="review.images"
            fit="cover"
            class="review-image"
          />
        </div>
        <div class="review-footer">
          <span class="review-time">{{ formatDate(review.created_at) }}</span>
        </div>
      </div>
    </div>

    <div class="pagination">
      <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pageSize"
        :total="total"
        layout="prev, pager, next"
        @current-change="handlePageChange"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { getProductReviews } from '@/api/products'
import { formatDate } from '@/utils/date'

const props = defineProps({
  productId: {
    type: [String, Number],
    required: true
  }
})

const reviews = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)

const averageRating = computed(() => {
  if (!reviews.value.length) return 0
  const sum = reviews.value.reduce((acc, review) => acc + review.rating, 0)
  return (sum / reviews.value.length).toFixed(1)
})

const fetchReviews = async () => {
  try {
    const response = await getProductReviews(props.productId, {
      page: currentPage.value,
      page_size: pageSize.value
    })
    reviews.value = response.data.results
    total.value = response.data.count
  } catch (error) {
    console.error('Failed to fetch reviews:', error)
  }
}

const handlePageChange = (page) => {
  currentPage.value = page
  fetchReviews()
}

onMounted(() => {
  fetchReviews()
})
</script>

<style scoped>
.product-reviews {
  padding: 20px;
  background: #fff;
  border-radius: 4px;
}

.reviews-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.review-item {
  padding: 20px 0;
  border-bottom: 1px solid #eee;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.username {
  font-weight: bold;
}

.review-content {
  margin: 10px 0;
  line-height: 1.6;
}

.review-images {
  display: flex;
  gap: 10px;
  margin: 10px 0;
}

.review-image {
  width: 100px;
  height: 100px;
  border-radius: 4px;
}

.review-footer {
  margin-top: 10px;
  color: #999;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
</style> 