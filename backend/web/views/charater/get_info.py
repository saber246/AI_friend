from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models.character import Character


class GetInfoCharacterView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def get(self, request):
        try:
            character_id = request.GET.get('character_id')
            character = Character.objects.get(id=character_id, author__user=request.user)
            return Response({
                'result': 'success',
                'character': {
                    'id': character_id,
                    'name': character.name,
                    'photo': character.photo.url,
                    'profile': character.profile,
                    'background': character.background.url,
                }
            })
        except:  # noqa: E722
            return Response({'error': 'get charater info error'}, status=500) 