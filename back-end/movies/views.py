from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Movie, Comment, Genre, Actor, Director
from .serializers import UserSerializer, MovieSerializer, CommentSerializer, CommentCreateSerializer, GenreSerializer, ActorSerializer, DirectorSerializer, UserDetailSerializer
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Sucess Create ID')


@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    movies = Movie.objects.all().order_by('-pk')
    movies = movies[0:10]
    movies = sorted(movies, key=lambda movie: -movie.score)
    serializer = MovieSerializer(many=True, instance=movies)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    # view
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk, user_id=request.user.id)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    keyword = request.GET.get('keyword', '')

    movies = Movie.objects.all()

    if keyword:
        movies = movies.filter(title__icontains=keyword)
    serializer = MovieSerializer(many=True, instance=movies)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentCreateSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        comment.delete()
        # 요청에 성공했지만 컨텐츠는 없다는걸 알려주는 status code
        return Response(status=204)


@api_view(['GET'])
@permission_classes([AllowAny])
def genredb(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(instance=genre)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def actordb(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(instance=actor)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def directordb(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)
    serializer = DirectorSerializer(instance=director)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def userdetaildb(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def userdetaildball(request):
    users = User.objects.all()
    serializer = UserDetailSerializer(many=True, instance=users)
    return Response(serializer.data)


@api_view(['POST'])
def survey(request):
    serializer = UserDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)