from django.urls import path
from .views import (
    MovieListView, MovieDetailView, DirectorListView, DirectorDetailView,
    ReviewListView, ReviewDetailView, UserRegisterView, UserLoginView
)

urlpatterns = [
    # Список и детали фильмов
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),

    # Список и детали режиссёров
    path('directors/', DirectorListView.as_view(), name='director_list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),

    # Список и детали отзывов
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),

    # Register and Login
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
