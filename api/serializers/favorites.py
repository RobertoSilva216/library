from rest_framework import serializers
from api.models.favorites import Favorites


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['user', 'book']


class FavoriteSerializerOut(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Favorites
        fields = ['username', 'book', 'book_title']
