from django.shortcuts import render
from django.views.generic import ListView
from movie_app.models import Movie, Director, Review
from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_app_cbv/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_app_cbv/movie_detail.html'
    context_object_name = 'movie'

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

class DirectorListView(ListView):
    model = Director
    template_name = 'movie_app_cbv/director_list.html'
    context_object_name = 'directors'

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'movie_app_cbv/director_detail.html'
    context_object_name = 'director'

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

class ReviewListView(ListView):
    model = Review
    template_name = 'movie_app_cbv/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'movie_app_cbv/review_detail.html'
    context_object_name = 'review'

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Вы успешно зарегистрировались.",
                    "token": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            return Response(
                {
                    "message": "Вы успешно авторизовались.",
                    "access": data.get("access"),
                    "refresh": data.get("refresh"),
                },
                status=status.HTTP_200_OK,
            )
        return response

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

