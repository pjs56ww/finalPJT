from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    path('signup/', views.signup), 

    # 기본 page
    path('home/', views.home),
    
    # 영화 상세보기
    path('movies/<int:movie_pk>/', views.movie_detail),

    # 댓글 url
    path('movies/<int:movie_pk>/comment/', views.comment_create),

    # 검색
    path('search/', views.search),
]
