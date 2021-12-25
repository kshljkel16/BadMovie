from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.base import View

from .models import Movie, Category, Rating, Reviews
from .forms import ReviewForm, RatingForm
# from account.forms import UserRegisterForm, UserUpdateForm


class MoviesView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    print(queryset)

    template_name = "movie/homev3.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        return context


class MovieDetailView(DetailView):

    model = Movie
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        # context["form"] = ReviewForm()
        return context


class MoviesListView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movie/homev3.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs['register'] = UserRegisterForm
        return qs


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent",None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie_id = movie.pk
            form.save()
        return redirect(movie.get_absolute_url())



class MovieSearchView(View):
    def get(self, request, search_word):
        queryset = Movie.objects.filter(title__icontains=search_word)
        print(queryset)
        return render(request, "movie/search_movie.html", context={'movie_list':queryset})

    def post(self, request):
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
        data = request.POST
        word = data['search_word']
        print(word)
        return redirect('search-find', search_word=word)


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        print('SLLLLLLLL')
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            print('OK')
            return 'OK'
        else:
            return HttpResponse(status=400)


class CommentDelete(DeleteView):
    model = Reviews
    template_name = 'movie/delete_product.html'
    success_url = reverse_lazy('home')