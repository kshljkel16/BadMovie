from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    print(queryset)
    queryset = queryset[:5]
    template_name = "movie/homev3.html"


class MovieDetailView(DetailView):

    model = Movie
    slug_field = "url"


class MoviesListView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movie/homev3.html"