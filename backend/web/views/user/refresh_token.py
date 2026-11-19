from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result': 'error',
                    'message': '刷新令牌不存在'
                }, status=400)
            refresh = RefreshToken(refresh_token)
            user = User.objects.get(id=refresh['user_id'])
            user_profile = UserProfile.objects.get(user=user)
            if settings.SIMPLE_JWT['BLACKLIST_AFTER_ROTATION']:
                refresh.set_jti()
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.pk,
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
            return ({
                'result': 'success',
                'access': str(refresh.access_token),
            })
        except:  # noqa: E722
            return Response({
                'result': 'error',
                'message': '刷新令牌不能为空'        
            }, status = 401)