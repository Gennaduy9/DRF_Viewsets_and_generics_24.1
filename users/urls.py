from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, UserUpdateView

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update')
] + router.urls