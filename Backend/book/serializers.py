from rest_framework.serializers import ModelSerializer
from core.models import Book,Purchase,Category,Author


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PurshaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'                