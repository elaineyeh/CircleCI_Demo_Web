from django.db import models
from django.contrib.auth.models import User


class SeriesName(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_user')
    description = models.TextField(blank=True, null=True)
    series_name = models.ManyToManyField(SeriesName)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title