import imp
import django_filters
from .models import Movie, MovieCatelog

# filter class for movie catelog
class MovieCatelogFilter(django_filters.FilterSet):
    class Meta:
        model = MovieCatelog
        fields = ['movie_catelog_title', 'movie_catelog_description']

# filter class for movie
class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['movie_title', 'movie_genre', 'movie_duration', 'movie_director', 'movie_cast', 'movie_language', 'movie_country', 'movie_awards', 'movie_imdb_rating', 'movie_imdb_votes', 'movie_imdb_id', 'movie_metascore', 'movie_boxoffice', 'movie_production']


        