from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    path('signup/', views.signup), 

    # 기본 page
    path('home/', views.home),
    
    # 영화 상세보기
    path('movies/<int:movie_pk>/', views.movie_detail),

    # 댓글 생성
    path('movies/<int:movie_pk>/comment/', views.comment_create),

    # 댓글 수정, 삭제
    path('comment/<int:comment_pk>/', views.comment_update_delete),

    # 검색
    path('search/', views.search),

    # DB 전송
    path('genredb/<int:genre_pk>/', views.genredb),

    path('directordb/<int:director_pk>/', views.directordb),

    path('actordb/<int:actor_pk>/', views.actordb),

    # User정보 전송
    path('userdetaildb/<int:user_pk>/', views.userdetaildb),

    # 모든 데이터 전송
    path('userdetaildb/', views.userdetaildball),
    
    # 설문 조사 데이터 전송
    path('survey/', views.survey),

]
