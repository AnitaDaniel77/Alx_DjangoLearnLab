from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

>>>>>>> 5b4842a05845136b4460cd1b3146030f79c267bb
