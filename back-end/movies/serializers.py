from rest_framework import serializers
from .models import Movie, Comment, Genre, Actor, Director, User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movieCd', 'title', 'description', 'image', 'pubdate', 'score', 'backgroundImage')


class FollowerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user__username')

    class Meta:
        model = User
        fields = ('username', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True)
    followers = FollowerSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'followers')


class CommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'movie', 'user',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'movie_id', 'user_id',)


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ('id', 'genreNm', 'movies',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = ('id', 'name', 'movies',)

        