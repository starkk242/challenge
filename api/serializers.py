from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','is_active', 'is_superuser','is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, user, validated_data):
        user.is_active = validated_data.get('is_active', user.is_active)
        user.save()
        return user
    
    def multi_update(self,user):
        return user

    def delete_user(self):
        self.delete()
        return 