from django.urls import path
from .views import *

urlpatterns = [
    # category
    path('add-category', CreateCategoryAPIView.as_view()),
    path('list-categories', ListCategoriesAPIView.as_view()),
    # articles
    path('add-article', CreateArticleAPIView.as_view()),
    path('delete-article/<int:id>', DeleteArticleAPIView.as_view()),
    path('list-most-liked-articles', ListMostLikesArticlesAPIView.as_view()),
    path('list-articles-by-category/<int:id>', ListArticlesByCategoryAPIView.as_view()),
    # bookmarks
    path('add-bookmark', CreateBookMarkAPIView.as_view()),
    path('list-user-bookmarks/<int:id>', ListUserBookmarksAPIView.as_view()),
]
