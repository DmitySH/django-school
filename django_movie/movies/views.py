from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return set(map(lambda x: x[0],
                       Movie.objects.filter(draft=False).values_list('year')))


class MovieView(ListView, GenreYear):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movie_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(DetailView, GenreYear):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_detail.html'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            # form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView, GenreYear):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class FilterMoviesView(ListView, GenreYear):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        ).distinct()
        return queryset
