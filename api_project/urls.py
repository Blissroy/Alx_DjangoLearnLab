from django.contrib import admin
from django.urls import path, include  # Make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This is the critical line that's missing
]
