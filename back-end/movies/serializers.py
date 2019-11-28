from rest_framework import serializers
from .models import Movie, Comment, Genre, Actor, Director, User



class FollowerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user__username')

    class Meta:
        model = User
        fields = ('username', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'survey', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            survey = False,
            genre = ''
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'survey')

class CommentSerializer(serializers.ModelSerializer):

    user = UserSecuritySerializer()
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'user')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    like_users = UserSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    class Meta:
        model = Movie
        
        fields = ('id', 'movieCd', 'title', 'genres', 'directors', 'actors', 'description', 'image', 'openDt', 'audiAcc', 'score', 'backgroundImage', 'comments', 'like_users')


class UserCommentSerializer(serializers.ModelSerializer):

    user = UserSecuritySerializer()
    movie = MovieSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'user', 'movie')


# 유저 자세 정보
class UserDetailSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True)
    followers = FollowerSerializer(many=True)
    comments = UserCommentSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'followers', 'comments', 'survey')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'movie_id', 'user_id',)


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ('id', 'genreNm', 'movies',)


# 배우 기준 정보 찾을 때 필요
class ActorMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)


# 감독 기준 정보 찾을 때 필요
class DirectorMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = ('id', 'name', 'movies',)