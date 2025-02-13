from rest_framework.serializers import ModelSerializer
from core.models import Book,Purchase


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PurshaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'        