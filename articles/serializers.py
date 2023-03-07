from rest_framework.serializers import ModelSerializer
from .models import Category, Article, Bookmark


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CreateArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class GetArticleSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = '__all__'


class BookmarkSerializer(ModelSerializer):
    article = GetArticleSerializer()

    class Meta:
        model = Bookmark
        fields = '__all__'
