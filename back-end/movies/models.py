from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')


class Genre(models.Model):
    genreNm = models.CharField(max_length=150)


class Movie(models.Model):
    movieCd = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=150)
    directors = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    pubdate = models.CharField(max_length=12)
    score = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    genres = models.ManyToManyField(Genre, related_name="movies")
    like_users = models.ManyToManyField(User, related_name="like_movies")
    

class Comment(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
