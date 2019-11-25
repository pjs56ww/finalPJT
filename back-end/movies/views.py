from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Movie
from .serializers import UserSerializer, MovieSerializer
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