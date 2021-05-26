from rest_framework import viewsets
from django.contrib.auth.models import User
from api import serializers
from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import ast


@authentication_classes([])
@permission_classes([])
class UserViewSet(viewsets.ModelViewSet):
    # User view
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


@authentication_classes([])
@permission_classes([])
class ModelUpdate(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request):
        user_list = request.data['user_list']
        state = request.data['state']
        print(user_list)
        user_list = ast.literal_eval(user_list)
        for i in user_list:
            user_id = int(i)
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=None)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            user.is_active=state
            user.save()
        return Response(user.is_active)

    def delete(self, request):
        user_list = request.data['user_list']
        user_list = ast.literal_eval(user_list)
        for i in user_list:
            user_id = int(i)
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=None)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            user.delete()
        return Response("Deleted")
            


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



