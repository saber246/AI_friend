from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            if not username or not password:
                return Response({
                    'result': 'error',
                    'message': '用户名或密码不能为空'
                }, status=400,
            )
            
            user = authenticate(username=username, password=password)
            if user is not None:
                user_profile = UserProfile.objects.get(user=user)
                refresh = RefreshToken.for_user(user)
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.pk, # type: ignore
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                })
                response.set_cookie(
                    key = 'refresh_token',
                    value = str(refresh),
                    httponly = True,
                    samesite = 'Lax',
                    secure = not settings.DEBUG,
                    max_age = 60 * 60 * 24 * 7
                )
                return response
            return Response({
                'result': 'error',
                'message': '用户名或密码错误',
            })
                
        except:  # noqa: E722
            return Response({'error': '系统异常，请联系管理员。'}, status=400)