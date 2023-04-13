from django.db.models import Count
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .models import Category, Article, Bookmark
from .serializers import CategorySerializer, CreateArticleSerializer, GetArticleSerializer, BookmarkSerializer


# Category
class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategoriesAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Article
class CreateArticleAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer


class DeleteArticleAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    lookup_field = 'id'


# Article
class ListMostLikesArticlesAPIView(ListAPIView):
    """
    List of Articles that has the largest number of likes
    """
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer

    def get_queryset(self):
        """
        :return: the first 5 query articles sorted by the likes count
        """
        return self.queryset.annotate(l_count=Count('likes')).order_by('-l_count')[:5]


class ListArticlesByCategoryAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        category_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(category_id=category_id)


# Bookmark
class CreateBookMarkAPIView(CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class ListUserBookmarksAPIView(ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(user_id=user_id)
