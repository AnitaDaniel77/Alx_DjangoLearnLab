from datetime import datetime
from rest_framework import serializers
from .models import Author, Book

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model

    # Custom validation: ensure publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: include all books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Show author name and their books

