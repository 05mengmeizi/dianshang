<template>
  <div class="footer">
    <div class="footer-content">
      <div class="footer-section">
        <h3>关于我们</h3>
        <ul>
          <li><a href="#">公司简介</a></li>
          <li><a href="#">联系我们</a></li>
          <li><a href="#">加入我们</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>帮助中心</h3>
        <ul>
          <li><a href="#">购物指南</a></li>
          <li><a href="#">支付方式</a></li>
          <li><a href="#">配送方式</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>售后服务</h3>
        <ul>
          <li><a href="#">退货政策</a></li>
          <li><a href="#">退货流程</a></li>
          <li><a href="#">常见问题</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>关注我们</h3>
        <div class="social-links">
          <a href="#"><i class="el-icon-weixin"></i></a>
          <a href="#"><i class="el-icon-weibo"></i></a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024 电商平台. All rights reserved.</p>
    </div>
  </div>
</template>

<style scoped>
.footer {
  background: #f5f5f5;
  padding: 40px 0 20px;
  margin-top: 40px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  padding: 0 20px;
}

.footer-section h3 {
  font-size: 18px;
  margin-bottom: 20px;
  color: #333;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 10px;
}

.footer-section ul li a {
  color: #666;
  text-decoration: none;
}

.footer-section ul li a:hover {
  color: #409EFF;
}

.social-links {
  display: flex;
  gap: 15px;
}

.footer-bottom {
  text-align: center;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid #ddd;
}

.footer-bottom p {
  color: #999;
}
</style> 