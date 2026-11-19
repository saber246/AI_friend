from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password1 = request.data.get('password1')
            password2 = request.data.get('password2')
            if username is None or password1 is None:
                return Response({
                    'result': 'error',
                    'message': '用户名或密码不能为空',
                }, status=400,
            )
                
            if password1 != password2:
                return Response({
                    'result': 'error',
                    'message': '两次密码不一致',
                }, status=400,
            )
            
            user = User.objects.create_user(username=username, password=password1)
            user_profile = UserProfile.objects.create(user=user)
            
            refresh = RefreshToken.for_user(user)
            resopnse = Response({
                'result': 'success',
                'access': str(refresh.access_token),
                'user_id': user.pk, # type: ignore
                'username': user.username,
                'photo': user_profile.photo.url,
                'profile': user_profile.profile,
            })
            resopnse.set_cookie(
                key = 'refresh_token',
                value = str(refresh),
                httponly = True,
                samesite = 'Lax',
                secure = not settings.DEBUG,
                max_age = 60 * 60 * 24 * 7
            )
            return resopnse
        
        except:  # noqa: E722
            return Response({
                'result': 'error',
                'message': '系统异常，请联系管理员。',
            })
    