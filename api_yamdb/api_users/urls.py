from django.urls import include, path
from rest_framework import routers

from api_users.views import UserApiViewSet, get_token, signup


app_name = 'api_users'
router = routers.DefaultRouter()
router.register(
    'users',
    UserApiViewSet,
    basename='user'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='token'),
]
