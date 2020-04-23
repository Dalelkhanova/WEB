from rest_framework import serializers
from .models import Category, Books, Card


class CategoriesListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category()
        category.name = validated_data.get('name', 'default name')
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class BooksListSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.id')

    class Meta:
        model = Books
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    clothes = BooksListSerializer(many=True)

    class Meta:
        model = Card
        fields = {'id', 'books'}