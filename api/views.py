from rest_framework import viewsets
from django.contrib.auth.models import User
from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer