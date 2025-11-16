from django.urls import path, include

urlpatterns = [
    ...
    path('auth/', include('relationship_app.urls')),
]

