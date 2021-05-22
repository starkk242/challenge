from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from api import serializers
from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status



@authentication_classes([])
@permission_classes([])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def put(self, request, *args, **kwargs):
        user = request.data["pk"]
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        user = request.data["pk"]
        serializer = UserSerializer(user, data=request.data)
        #user.delete()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return self.destroy(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@authentication_classes([])
@permission_classes([])
class EditView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def put(self, request, format=None):
        user = request.data["username"]
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        user = request.data["username"]
        serializer = UserSerializer(user, data=request.data)
        #user.delete()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)



