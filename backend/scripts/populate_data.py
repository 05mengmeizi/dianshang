import os
import django
import sys

# 设置 Django 环境
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.products.models import Category, Product

def create_sample_data():
    # 创建商品分类
    categories = [
        {
            'name': '粮油作物',
            'description': '各类粮食作物和油料作物'
        },
        {
            'name': '新鲜蔬菜',
            'description': '当季新鲜蔬菜'
        },
        {
            'name': '时令水果',
            'description': '应季水果'
        },
        {
            'name': '禽蛋产品',
            'description': '散养禽蛋类产品'
        }
    ]

    # 创建分类
    created_categories = []
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        created_categories.append(category)
        if created:
            print(f"创建分类: {category.name}")
        else:
            print(f"分类已存在: {category.name}")

    # 创建商品数据
    products = [
        {
            'name': '有机大米',
            'description': '东北黑土地有机大米，无农药残留，自然生长',
            'price': 99.00,
            'stock': 1000,
            'image': 'products/rice.jpg',
            'category': created_categories[0]  # 粮油作物
        },
        {
            'name': '新鲜玉米',
            'description': '当季新鲜玉米，产地直供，甜度高',
            'price': 15.90,
            'stock': 500,
            'image': 'products/corn.jpg',
            'category': created_categories[0]  # 粮油作物
        },
        {
            'name': '有机胡萝卜',
            'description': '新鲜采摘胡萝卜，富含胡萝卜素',
            'price': 8.80,
            'stock': 300,
            'image': 'products/carrot.jpg',
            'category': created_categories[1]  # 新鲜蔬菜
        },
        {
            'name': '新鲜西红柿',
            'description': '温室栽培西红柿，个大汁多',
            'price': 12.80,
            'stock': 400,
            'image': 'products/tomato.jpg',
            'category': created_categories[1]  # 新鲜蔬菜
        },
        {
            'name': '红富士苹果',
            'description': '陕西红富士苹果，脆甜多汁',
            'price': 28.80,
            'stock': 600,
            'image': 'products/apple.jpg',
            'category': created_categories[2]  # 时令水果
        },
        {
            'name': '麒麟瓜',
            'description': '海南麒麟瓜，香甜可口',
            'price': 32.90,
            'stock': 200,
            'image': 'products/melon.jpg',
            'category': created_categories[2]  # 时令水果
        },
        {
            'name': '散养土鸡蛋',
            'description': '农家散养土鸡蛋，蛋黄饱满',
            'price': 45.00,
            'stock': 1000,
            'image': 'products/eggs.jpg',
            'category': created_categories[3]  # 禽蛋产品
        },
        {
            'name': '生态鸭蛋',
            'description': '散养生态鸭蛋，营养丰富',
            'price': 48.00,
            'stock': 800,
            'image': 'products/duck-eggs.jpg',
            'category': created_categories[3]  # 禽蛋产品
        }
    ]

    # 创建商品
    for prod_data in products:
        product, created = Product.objects.get_or_create(
            name=prod_data['name'],
            defaults={
                'description': prod_data['description'],
                'price': prod_data['price'],
                'stock': prod_data['stock'],
                'image': prod_data['image'],
                'category': prod_data['category']
            }
        )
        if created:
            print(f"创建商品: {product.name}")
        else:
            print(f"商品已存在: {product.name}")

if __name__ == '__main__':
    print("开始创建示例数据...")
    create_sample_data()
    print("示例数据创建完成！") 