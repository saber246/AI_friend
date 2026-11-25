from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import index
from .views.charater.create import CreateCharacterView
from .views.charater.get_info import GetInfoCharacterView
from .views.charater.remove import RemoveCharacter
from .views.charater.update import UpdateCharacterView
from .views.profile.update import UpdateProfile
from .views.user.get_user_info import GetUserInfoView
from .views.user.login import LoginView
from .views.user.logout import LogoutView
from .views.user.refresh_token import RefreshTokenView
from .views.user.register import RegisterView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', index.index, name='index'),
    path('api/user/login/', LoginView.as_view(), name='login'),
    path('api/user/register/', RegisterView.as_view(), name='register'),
    path('api/user/refresh/', RefreshTokenView.as_view(), name='refresh'),
    path('api/user/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/info/', GetUserInfoView.as_view(), name='get_user_info'),
    path('api/profile/update/', UpdateProfile.as_view(), name='update_profile'),
    path('api/create/character/get_info/', GetInfoCharacterView.as_view(), name='get_character_info'),
    path('api/create/character/remove/', RemoveCharacter.as_view(), name='remove_character'),
    path('api/create/character/create/', CreateCharacterView.as_view(), name='create_character'),
    path('api/create/character/update/', UpdateCharacterView.as_view(), name='update_character'),
   
]