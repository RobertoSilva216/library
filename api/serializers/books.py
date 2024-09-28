from rest_framework import serializers
from api.models.books import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookSerializerOut(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'author_name', 'description']
