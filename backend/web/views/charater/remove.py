from rest_framework.permissions import IsAuthenticated  # noqa: F401, RUF100
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.character import Character
from web.models.user import UserProfile  # noqa: F401


class RemoveCharacter(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def post(self, request):
        try:
            character_id = request.data.get('character_id')
            character = Character.objects.get(id=character_id)
            if character.author.user_id != request.user.user_id:
                return Response({'error': '你没有创建这个角色'}, status=403)
            character.delete()
            return Response({'message': 'remove charater success'})
        except:  # noqa: E722
            return Response({'error': 'remove charater error'}, status=500) 
