from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework.authtoken.models import Token




class UserSerializer(serializers.ModelSerializer):
class Meta:
model = User
fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture')
read_only_fields = ('id',)




class RegisterSerializer(serializers.ModelSerializer):
password = serializers.CharField(write_only=True, required=True, min_length=8)


class Meta:
model = User
fields = ('username', 'email', 'password', 'first_name', 'last_name', 'bio')


def create(self, validated_data):
password = validated_data.pop('password')
user = User(**validated_data)
user.set_password(password)
user.save()
# create token
Token.objects.create(user=user)
return user




class LoginSerializer(serializers.Serializer):
username = serializers.CharField()
password = serializers.CharField(write_only=True)


def validate(self, data):
username = data.get('username')
password = data.get('password')
if username and password:
user = authenticate(username=username, password=password)
if user:
data['user'] = user
return data
raise serializers.ValidationError('Unable to log in with provided credentials.')
