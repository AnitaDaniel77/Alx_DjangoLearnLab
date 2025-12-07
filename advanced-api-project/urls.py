from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Project-level URL configuration
urlpatterns = [
    path('admin/', admin.site.urls),             # Django admin panel
    path('', include('api.urls')),               # Include API app routes
    path('api-token-auth/', obtain_auth_token),  # Token login endpoint
    path('', include('api.urls')),  # Include API app routes
]
