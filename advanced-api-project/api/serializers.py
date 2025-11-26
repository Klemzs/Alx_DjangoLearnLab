from datetime import datetime
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = '__all__'  # Serializes all fields of the Book model

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future

        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)  # Nested BookSerializer for related books

    class Meta:
        model = Author
        fields = ['name','books']   # Includes name field and nested books

