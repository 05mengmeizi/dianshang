 # API 文档

## 基础信息

- 基础URL: `http://localhost:8000/api`
- 所有请求都需要在 header 中携带 token: `Authorization: Bearer {token}`
- 响应格式: JSON
- 时间格式: ISO 8601 (YYYY-MM-DDTHH:mm:ss.sssZ)

## 认证相关

### 用户注册

```
POST /users/register/
```

请求参数：
```json
{
  "phone": "13800138000",
  "password": "your_password",
  "confirm_password": "your_password"
}
```

响应：
```json
{
  "id": 1,
  "phone": "13800138000",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 用户登录

```
POST /users/login/
```

请求参数：
```json
{
  "phone": "13800138000",
  "password": "your_password"
}
```

响应：
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "phone": "13800138000"
  }
}
```

### 获取用户信息

```
GET /users/info/
```

响应：
```json
{
  "id": 1,
  "phone": "13800138000",
  "nickname": "用户昵称",
  "avatar": "avatar.jpg",
  "created_at": "2024-01-01T00:00:00.000Z"
}
```

## 商品相关

### 获取商品列表

```
GET /products/
```

查询参数：
- `page`: 页码 (默认: 1)
- `page_size`: 每页数量 (默认: 12)
- `category`: 分类ID
- `search`: 搜索关键词
- `min_price`: 最低价格
- `max_price`: 最高价格
- `sort`: 排序方式 (price_asc/price_desc/newest)

响应：
```json
{
  "count": 100,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "有机大米",
      "description": "东北黑土地有机大米",
      "price": "99.00",
      "stock": 1000,
      "image": "products/rice.jpg",
      "category": {
        "id": 1,
        "name": "粮油作物"
      },
      "created_at": "2024-01-01T00:00:00.000Z"
    }
  ]
}
```

### 获取商品详情

```
GET /products/{id}/
```

响应：
```json
{
  "id": 1,
  "name": "有机大米",
  "description": "东北黑土地有机大米",
  "price": "99.00",
  "stock": 1000,
  "image": "products/rice.jpg",
  "category": {
    "id": 1,
    "name": "粮油作物"
  },
  "created_at": "2024-01-01T00:00:00.000Z"
}
```

### 获取商品分类

```
GET /categories/
```

响应：
```json
[
  {
    "id": 1,
    "name": "粮油作物",
    "description": "各类粮食作物和油料作物"
  }
]
```

## 购物车相关

### 获取购物车

```
GET /cart/
```

响应：
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "有机大米",
        "price": "99.00",
        "image": "products/rice.jpg"
      },
      "quantity": 2,
      "total_price": "198.00"
    }
  ],
  "total_items": 2,
  "total_amount": "198.00"
}
```

### 添加商品到购物车

```
POST /cart/items/
```

请求参数：
```json
{
  "product_id": 1,
  "quantity": 2
}
```

响应：
```json
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "有机大米",
    "price": "99.00"
  },
  "quantity": 2,
  "total_price": "198.00"
}
```

### 更新购物车商品数量

```
PUT /cart/items/{id}/
```

请求参数：
```json
{
  "quantity": 3
}
```

响应：
```json
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "有机大米",
    "price": "99.00"
  },
  "quantity": 3,
  "total_price": "297.00"
}
```

### 删除购物车商品

```
DELETE /cart/items/{id}/
```

响应状态码：204

## 订单相关

### 获取订单列表

```
GET /orders/
```

查询参数：
- `page`: 页码
- `page_size`: 每页数量
- `status`: 订单状态 (pending/paid/shipped/completed/cancelled)

响应：
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "order_number": "202401010001",
      "status": "pending",
      "total_amount": "198.00",
      "items": [
        {
          "product": {
            "id": 1,
            "name": "有机大米",
            "price": "99.00"
          },
          "quantity": 2,
          "price": "99.00"
        }
      ],
      "shipping_address": {
        "name": "张三",
        "phone": "13800138000",
        "address": "北京市朝阳区xxx"
      },
      "created_at": "2024-01-01T00:00:00.000Z"
    }
  ]
}
```

### 创建订单

```
POST /orders/
```

请求参数：
```json
{
  "shipping_address": {
    "name": "张三",
    "phone": "13800138000",
    "address": "北京市朝阳区xxx"
  }
}
```

响应：
```json
{
  "id": 1,
  "order_number": "202401010001",
  "status": "pending",
  "total_amount": "198.00",
  "items": [
    {
      "product": {
        "id": 1,
        "name": "有机大米",
        "price": "99.00"
      },
      "quantity": 2,
      "price": "99.00"
    }
  ],
  "shipping_address": {
    "name": "张三",
    "phone": "13800138000",
    "address": "北京市朝阳区xxx"
  },
  "created_at": "2024-01-01T00:00:00.000Z"
}
```

### 获取订单详情

```
GET /orders/{id}/
```

响应：
```json
{
  "id": 1,
  "order_number": "202401010001",
  "status": "pending",
  "total_amount": "198.00",
  "items": [
    {
      "product": {
        "id": 1,
        "name": "有机大米",
        "price": "99.00"
      },
      "quantity": 2,
      "price": "99.00"
    }
  ],
  "shipping_address": {
    "name": "张三",
    "phone": "13800138000",
    "address": "北京市朝阳区xxx"
  },
  "created_at": "2024-01-01T00:00:00.000Z",
  "paid_at": null,
  "shipped_at": null,
  "completed_at": null
}
```

### 取消订单

```
POST /orders/{id}/cancel/
```

响应：
```json
{
  "id": 1,
  "status": "cancelled",
  "cancelled_at": "2024-01-01T00:00:00.000Z"
}
```

## 错误响应

所有接口在发生错误时都会返回统一格式的错误响应：

```json
{
  "code": "ERROR_CODE",
  "message": "错误描述信息"
}
```

常见错误码：
- `401`: 未认证
- `403`: 无权限
- `404`: 资源不存在
- `400`: 请求参数错误
- `500`: 服务器内部错误

## 注意事项

1. 所有涉及金额的字段都使用字符串类型，避免浮点数精度问题
2. 分页接口都支持 `page` 和 `page_size` 参数
3. 时间戳都使用 ISO 8601 格式
4. 文件上传接口都使用 multipart/form-data 格式
5. 所有接口都需要在请求头中携带 token（除了登录和注册接口）