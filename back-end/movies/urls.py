from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup), 
    path('home/', views.home),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comment/', views.comment_create),
]
