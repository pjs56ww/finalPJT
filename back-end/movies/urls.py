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
]
