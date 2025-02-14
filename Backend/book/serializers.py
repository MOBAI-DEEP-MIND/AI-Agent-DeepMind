from rest_framework.serializers import ModelSerializer
from core.models import Book,Purchase,Category,Author, Busket
import rest_framework.serializers as serializers


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
 
class BookSearchSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['query']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'       

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['user','book','number_books','credit_card_number','cvv','expiration_date']
        extra_kwargs = {'user': {'read_only': True}}


class BusketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busket
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}