from django.urls import path, include, re_path
from . import consumers
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView,
)


router = routers.DefaultRouter()

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls')),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
  path('index/', views.IndexView.as_view(), name='index'),
]

websocket_urlpatterns = [
  re_path(r'ws/websocket-server/(?P<room_name>\w+)/$', consumers.WSConsumer.as_asgi()),
]
