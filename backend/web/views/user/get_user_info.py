from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class GetUserInfoView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    def get(self, request):
        user = request.user
        user_profile = user.userprofile
        return Response({
            'result': 'success',
            'user_id': user.id,
            'username': user.username,
            'phone': user_profile.phone.url,
            'profile': user_profile.profile,
        })
