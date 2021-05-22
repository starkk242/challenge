from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from api.views import EditView, UserViewSet,RegisterView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change/',EditView.as_view()),
]