from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api.views import UserViewSet,RegisterView,ModelUpdate

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('act/', ModelUpdate.as_view())
]