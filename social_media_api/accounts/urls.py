from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, ProfileView, PublicProfileView


urlpatterns = [
path('register/', RegisterView.as_view(), name='register'),
path('login/', CustomObtainAuthToken.as_view(), name='login'),
path('profile/', ProfileView.as_view(), name='profile'),
# public profile by username: /accounts/users/<username>/
path('users/<str:username>/', PublicProfileView.as_view(), name='public-profile'),
]
