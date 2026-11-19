from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.user import UserProfile


def remove_photo(photo):
    if photo and photo.name != 'user/photos/default.jpg':
        old_path = settings.MEDIA_ROOT / photo.name
        if old_path.exists():
            old_path.remove()


class UpdateProfile(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            username = request.data.get('username')
            profile = request.data.get('profile')
            photo = request.FILES.get('photo', None)
            if not username or not profile:
                return Response({
                    'result': '用户名或简介不能为空',
                })
            if username == user.username:
                return Response({
                    'result': '用户名不能与当前用户名相同',
                })
            if User.objects.filter(username=username).exists():
                return Response({
                    'result': '用户名已存在',
                })
            if photo:
                remove_photo(user_profile.photo)
                user_profile.photo = photo
            user_profile.save()
            user.save()
            return Response({
                'result': '更新成功',
                'user_id': user.id,
                'username': username,
                'profile': profile,
                'photo': user_profile.photo.url,
            })
                
                
        
        except Exception as e:  # noqa: BLE001
            return Response({
                'error': str(e),
                'result': '服务器异常，请稍候重试',
                'status': 500
            })
