from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        
        # 分类过滤
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category_id=category)
        
        # 价格范围过滤
        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)
        if price_min is not None:
            queryset = queryset.filter(price__gte=price_min)
        if price_max is not None:
            queryset = queryset.filter(price__lte=price_max)
        
        # 搜索
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        
        # 排序
        sort = self.request.query_params.get('sort', None)
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'newest':
            queryset = queryset.order_by('-created_at')
            
        return queryset

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(f"Found {queryset.count()} categories") # 添加调试信息
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 添加商品详情视图
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class FeaturedProductsView(generics.ListAPIView):
    queryset = Product.objects.all()[:5]  # 简单示例，获取前5个商品
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

# 添加商品评论视图
class ProductReviewsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk']) 