from rest_framework import serializers
from .models import Movie, Comment, Genre, Actor, Director, User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movieCd', 'title', 'description', 'image', 'pubdate', 'score',)


class FollowerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user__username')

    class Meta:
        model = User
        fields = ('username', )


class UserSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=true)
    followers = FollowerSerializer(many=true)
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'followers')


class CommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserDetailSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'movie', 'user',)


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=true)
    class Meta:
        model = Genre
        fields = ('id', 'genreNm', 'movies',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=true)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=true)
    class Meta:
        model = Director
        fields = ('id', 'name', 'movies',)