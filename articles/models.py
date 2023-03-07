from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300, unique=True)
    cover_image = models.ImageField(upload_to='articles/cover/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_of_publish = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('authentication.User')
    body = models.TextField()

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title
