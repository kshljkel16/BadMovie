from django.urls import path

from . import views


urlpatterns = [
    path('', views.MovieSearchView.as_view(), name='search'),
    path('<str:search_word>/', views.MovieSearchView.as_view(), name='search-find'),
]
