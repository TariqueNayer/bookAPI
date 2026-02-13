from rest_framework import serializers
from .models import Book, Order

class AdminBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book 
        fields = ['id', 'title', 'pdf_file','author', 'description', 'price']

class PublicBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book 
        fields = ['id', 'title', 'author', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    # This automatically add the tag if the book is gone ma boy
    book_info = serializers.ReadOnlyField(source='book_display_info')

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'book_info', 'price', 'status']