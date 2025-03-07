from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from django.middleware.csrf import get_token
from .models import User

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        
        if not phone or not password:
            return Response({
                'message': '手机号和密码不能为空'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            user = User.objects.get(phone=phone)
            if user.check_password(password):
                login(request, user)
                return Response({
                    'message': '登录成功',
                    'user': {
                        'id': user.id,
                        'phone': user.phone,
                        'avatar': user.avatar.url if user.avatar else None
                    },
                    'csrfToken': get_token(request)
                })
            else:
                return Response({
                    'message': '密码错误'
                }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({
                'message': '用户不存在'
            }, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '已退出登录'})

class CheckLoginStatusView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                'isLoggedIn': True,
                'user': {
                    'id': request.user.id,
                    'phone': request.user.phone,
                    'avatar': request.user.avatar.url if request.user.avatar else None
                }
            })
        return Response({'isLoggedIn': False})

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # 创建用户
            user = serializer.save()
            # 生成token
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': '注册成功',
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInfoView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data) 