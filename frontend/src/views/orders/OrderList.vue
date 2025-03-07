<template>
  <div class="order-list">
    <h2>我的订单</h2>
    
    <el-table :data="orders" style="width: 100%">
      <el-table-column prop="id" label="订单号" width="180" />
      
      <el-table-column label="订单状态" width="120">
        <template #default="{ row }">
          <el-tag :type="getStatusType(row.status)">
            {{ getStatusText(row.status) }}
          </el-tag>
        </template>
      </el-table-column>
      
      <el-table-column prop="total_amount" label="总金额" width="120">
        <template #default="{ row }">
          ¥{{ row.total_amount }}
        </template>
      </el-table-column>
      
      <el-table-column prop="created_at" label="下单时间" width="180">
        <template #default="{ row }">
          {{ formatDate(row.created_at) }}
        </template>
      </el-table-column>
      
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button 
            type="primary" 
            size="small"
            @click="viewDetail(row.id)"
          >
            查看详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { getOrders } from '@/api/orders'
import { formatDate } from '@/utils/date'

const router = useRouter()
const orders = ref([])

const getStatusType = (status) => {
  const types = {
    pending: 'warning',
    paid: 'success',
    shipped: 'primary',
    completed: 'success',
    cancelled: 'danger'
  }
  return types[status] || 'info'
}

const getStatusText = (status) => {
  const texts = {
    pending: '待支付',
    paid: '已支付',
    shipped: '已发货',
    completed: '已完成',
    cancelled: '已取消'
  }
  return texts[status] || status
}

const viewDetail = (orderId) => {
  router.push(`/orders/${orderId}`)
}

const fetchOrders = async () => {
  try {
    const response = await getOrders()
    orders.value = response.data
  } catch (error) {
    ElMessage.error('获取订单列表失败')
  }
}

onMounted(() => {
  fetchOrders()
})
</script>

<style scoped>
.order-list {
  padding: 20px;
  background: #fff;
  border-radius: 4px;
}
</style> 