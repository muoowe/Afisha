from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, MovieViewSet, ReviewViewSet, registration, authorization

router = DefaultRouter()
router.register(r'directors', DirectorViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('auth/register/', registration, name='registration'),
    path('auth/login/', authorization, name='authorization'),
]
