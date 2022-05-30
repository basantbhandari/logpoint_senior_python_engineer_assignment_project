# Generated by Django 4.0.4 on 2022-05-29 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCatelog',
            fields=[
                ('movie_catelog_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_catelog_title', models.CharField(max_length=200)),
                ('movie_catelog_description', models.TextField()),
                ('movie_catelog_image', models.ImageField(upload_to='catelog/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=200)),
                ('movie_storyline', models.TextField()),
                ('movie_poster', models.ImageField(upload_to='posters/')),
                ('movie_trailer', models.URLField()),
                ('movie_rating', models.IntegerField()),
                ('movie_release_date', models.DateField()),
                ('movie_genre', models.CharField(max_length=200)),
                ('movie_duration', models.IntegerField()),
                ('movie_director', models.CharField(max_length=200)),
                ('movie_cast', models.CharField(max_length=200)),
                ('movie_language', models.CharField(max_length=200)),
                ('movie_country', models.CharField(max_length=200)),
                ('movie_awards', models.CharField(max_length=200)),
                ('movie_imdb_rating', models.IntegerField()),
                ('movie_imdb_votes', models.IntegerField()),
                ('movie_imdb_id', models.CharField(max_length=200)),
                ('movie_metascore', models.IntegerField()),
                ('movie_boxoffice', models.CharField(max_length=200)),
                ('movie_production', models.CharField(max_length=200)),
                ('movie_file', models.FileField(default=None, upload_to='movies/')),
                ('movie_belongto_catelog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.moviecatelog')),
            ],
        ),
    ]
