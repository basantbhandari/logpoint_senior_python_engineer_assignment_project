from django.db import models

# Create your models here.
# model for movie catelog
class MovieCatelog(models.Model):
    """
    some movie catelog information
    """
    movie_catelog_id = models.AutoField(primary_key=True)
    movie_catelog_title = models.CharField(max_length=200)
    movie_catelog_description = models.TextField()
    movie_catelog_image = models.ImageField(upload_to='catelog/')


# create model for Movie catelog blog

class Movie(models.Model):
    """
    some movie information
    """
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=200)
    movie_storyline = models.TextField()
    movie_poster = models.ImageField(upload_to='posters/')
    movie_trailer = models.URLField()
    movie_rating = models.IntegerField()
    movie_release_date = models.DateField()
    movie_genre = models.CharField(max_length=200)
    movie_duration = models.IntegerField()
    movie_director = models.CharField(max_length=200)
    movie_cast = models.CharField(max_length=200)
    movie_language = models.CharField(max_length=200)
    movie_country = models.CharField(max_length=200)
    movie_awards = models.CharField(max_length=200)
    movie_imdb_rating = models.IntegerField()
    movie_imdb_votes = models.IntegerField()
    movie_imdb_id = models.CharField(max_length=200)
    movie_metascore = models.IntegerField()
    movie_boxoffice = models.CharField(max_length=200)
    movie_production = models.CharField(max_length=200)
    movie_belongto_catelog = models.ForeignKey(MovieCatelog, on_delete=models.CASCADE)
    movie_file = models.FileField(upload_to='movies/', default=None)



