from django.contrib import admin
from .models import Movie, MovieCatelog

# Register your models here.

# register movie model
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'movie_release_date', 'movie_rating')
    list_filter = ('movie_release_date', 'movie_rating')
    search_fields = ('movie_title', 'movie_release_date', 'movie_rating')





# register movie catelog model
@admin.register(MovieCatelog)
class MovieCatelogAdmin(admin.ModelAdmin):
    list_display = ('movie_catelog_title', 'movie_catelog_description')
    list_filter = ('movie_catelog_title', 'movie_catelog_description')
    search_fields = ('movie_catelog_title', 'movie_catelog_description')