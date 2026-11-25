from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.character import Character


class UpdateCharacterView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def post(self, request):
        try:
            character_id = request.data.get('character_id')
            character = Character.objects.get(id=character_id)
            if character.author.user_id != request.user.user_id:
                return Response({'error': '你没有创建这个角色'}, status=403)
            name = request.data.get('name').strip()
            if name is not None:
                character.name = name
            photo = request.FILES.get('photo')
            if photo is not None:
                character.photo = photo
            profile = request.POST.get('profile').strip()
            if profile is not None:
                character.profile = profile
            background = request.data.get('background')
            if background is not None:
                character.background = background
            character.save()
            return Response({'message': 'update charater success'})
            
        
        except:  # noqa: E722
            return Response({'error': 'update charater error'}, status=500)