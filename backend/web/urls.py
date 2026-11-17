from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import index
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
    
]