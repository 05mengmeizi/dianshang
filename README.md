# 农产品商城

一个基于 Vue 3 和 Django 的现代农产品电商平台。专注于为农产品提供一个现代化的在线交易平台，连接农产品生产者和消费者。

## 技术栈

### 前端
- Vue 3 - 渐进式 JavaScript 框架
- Vue Router - 官方路由管理器
- Pinia - 新一代状态管理工具
- Element Plus - 基于 Vue 3 的组件库
- Vite - 现代前端构建工具
- Axios - HTTP 客户端
- ESLint - 代码检查工具
- Prettier - 代码格式化工具

### 后端
- Django 4.2 - Python Web 框架
- Django REST framework - RESTful API 工具
- SQLite/MySQL - 数据库
- Redis - 缓存和会话管理
- JWT - 用户认证
- Celery - 异步任务队列（计划中）

## 功能特性

### 已实现功能
- 用户认证
  - 手机号注册/登录
  - JWT 认证
  - 用户信息管理
- 商品管理
  - 商品分类
  - 商品搜索
  - 商品详情
  - 价格筛选
- 购物车
  - 添加/删除商品
  - 修改数量
  - 清空购物车
- 订单管理
  - 订单创建
  - 订单列表
  - 订单详情
- 个人中心
  - 个人信息修改
  - 订单历史
  - 收货地址管理

### 计划功能
- 支付集成
- 商品评价
- 收藏夹
- 商品推荐
- 售后服务

## 项目结构

```
├── frontend/                # Vue 3 前端项目
│   ├── src/
│   │   ├── api/            # API 接口定义
│   │   ├── assets/         # 静态资源
│   │   ├── components/     # 通用组件
│   │   │   ├── layout/     # 布局组件
│   │   │   └── products/   # 商品相关组件
│   │   ├── router/         # 路由配置
│   │   ├── stores/         # Pinia 状态管理
│   │   ├── styles/         # 全局样式
│   │   ├── utils/          # 工具函数
│   │   └── views/          # 页面组件
│   ├── public/             # 公共资源
│   └── package.json        # 项目配置
│
└── backend/                # Django 后端项目
    ├── apps/               # 应用目录
    │   ├── users/          # 用户管理
    │   ├── products/       # 商品管理
    │   ├── orders/         # 订单管理
    │   └── cart/           # 购物车
    ├── config/             # 项目配置
    ├── media/              # 媒体文件
    ├── static/             # 静态文件
    ├── requirements.txt    # Python 依赖
    └── manage.py          # Django 管理脚本
```

## 开始使用

### 环境要求
- Python 3.8+
- Node.js 16+
- MySQL 5.7+ (可选，默认使用 SQLite)
- Redis 6.0+

### 前端设置

```bash
# 克隆项目
git clone https://github.com/你的用户名/agricultural-mall.git

# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

### 后端设置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

## 开发规范

### Git 提交规范
- feat: 新功能
- fix: 修复
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试
- chore: 构建过程或辅助工具的变动

### 代码规范
- Python: 遵循 PEP 8
- JavaScript: 使用 ESLint + Prettier
- Vue: 遵循 Vue 官方风格指南

## 部署

### 前端部署
1. 构建生产版本
```bash
npm run build
```
2. 将 dist 目录下的文件部署到 Web 服务器

### 后端部署
1. 配置生产环境设置
2. 收集静态文件
```bash
python manage.py collectstatic
```
3. 使用 Gunicorn 运行应用
```bash
gunicorn config.wsgi:application
```

## 开发团队

- [你的名字] - 全栈开发

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目基于 MIT 许可证开源 - 查看 [LICENSE](LICENSE) 文件了解更多细节

