from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.character import Character
from web.models.user import UserProfile


class CreateCharacterView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            name = request.data.get('name').strip()
            profile = request.data.get('profile').strip()
            photo = request.FILES.get('photo')
            background = request.FILES.get('background')
            
            if not name:
                return Response({'error': '姓名不能为空'}, status=400)
            if not profile:
                return Response({'error': '个人介绍不能为空'}, status=400)
            if not photo:
                return Response({'error': '头像不能为空'}, status=400)
            if not background:
                return Response({'error': '背景不能为空'}, status=400)
            
            Character.objects.create(
                author=user_profile,
                name=name,
                photo=photo,
                peofile=profile,
                background=background,
            )
            
            return Response({'message': '创建成功'}, status=201)
            
            
        
        except:  # noqa: BLE001, E722, RUF100
            return Response({'error': 'create charater error'}, status=500)