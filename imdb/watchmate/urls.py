from django.urls import path
from watchmate.views import movie_details, movie_list

urlpatterns = [
    path('movie-json-list/', movie_list, name='movie-json-list'),
    path('movie-json-dtls/', movie_details, name='movie-json-dtls'),
]
