from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer




class RegisterView(generics.CreateAPIView):
serializer_class = RegisterSerializer
permission_classes = [permissions.AllowAny]


def create(self, request, *args, **kwargs):
serializer = self.get_serializer(data=request.data)
serializer.is_valid(raise_exception=True)
user = serializer.save()
token, _ = Token.objects.get_or_create(user=user)
data = UserSerializer(user).data
data['token'] = token.key
return Response(data, status=status.HTTP_201_CREATED)




class CustomObtainAuthToken(ObtainAuthToken):
def post(self, request, *args, **kwargs):
serializer = self.serializer_class(data=request.data,
context={'request': request})
serializer.is_valid(raise_exception=True)
user = serializer.validated_data['user']
token, created = Token.objects.get_or_create(user=user)
user_data = UserSerializer(user).data
return Response({'token': token.key, 'user': user_data})




class ProfileView(APIView):
permission_classes = [permissions.IsAuthenticated]


def get(self, request):
serializer = UserSerializer(request.user)
return Response(serializer.data)


def put(self, request):
serializer = UserSerializer(request.user, data=request.data, partial=True)
serializer.is_valid(raise_exception=True)
serializer.save()
return Response(serializer.data)




class PublicProfileView(generics.RetrieveAPIView):
queryset = User.objects.all()
serializer_class = UserSerializer
permission_classes = [permissions.AllowAny]
lookup_field = 'username'from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer




class RegisterView(generics.CreateAPIView):
serializer_class = RegisterSerializer
permission_classes = [permissions.AllowAny]


def create(self, request, *args, **kwargs):
serializer = self.get_serializer(data=request.data)
serializer.is_valid(raise_exception=True)
user = serializer.save()
token, _ = Token.objects.get_or_create(user=user)
data = UserSerializer(user).data
data['token'] = token.key
return Response(data, status=status.HTTP_201_CREATED)




class CustomObtainAuthToken(ObtainAuthToken):
def post(self, request, *args, **kwargs):
serializer = self.serializer_class(data=request.data,
context={'request': request})
serializer.is_valid(raise_exception=True)
user = serializer.validated_data['user']
token, created = Token.objects.get_or_create(user=user)
user_data = UserSerializer(user).data
return Response({'token': token.key, 'user': user_data})




class ProfileView(APIView):
permission_classes = [permissions.IsAuthenticated]


def get(self, request):
serializer = UserSerializer(request.user)
return Response(serializer.data)


def put(self, request):
serializer = UserSerializer(request.user, data=request.data, partial=True)
serializer.is_valid(raise_exception=True)
serializer.save()
return Response(serializer.data)




class PublicProfileView(generics.RetrieveAPIView):
queryset = User.objects.all()
serializer_class = UserSerializer
permission_classes = [permissions.AllowAny]
lookup_field = 'username'
