import imp
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
# import django form
from .forms import SignUpForm, LoginForm
#  import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Movie, MovieCatelog
from .filters import MovieFilter, MovieCatelogFilter



# Create your views here.
def welcome(request):
    return render(request, 'home/welcome.html')



def index(request):
    if request.user.is_authenticated:
        # take all the movies catelog from database
        movies_catelog = MovieCatelog.objects.all()
        # take all the movies from database
        print(movies_catelog)
        movies = Movie.objects.all()
        print(movies)
        # filter the movies catelog
        movies_catelog_filter = MovieCatelogFilter(request.GET, queryset=movies_catelog)
        # filter the movies
        movies_catelog = movies_catelog_filter.qs
        movies_filter = MovieFilter(request.GET, queryset=movies)
        # return the filtered movies catelog
        movies = movies_filter.qs
        return render(request, 'home/index.html', {'movies_catelog': movies_catelog, 'movies': movies, 'movies_catelog_filter': movies_catelog_filter, 'movies_filter': movies_filter})
    else:
        return HttpResponseRedirect('/')

# for view signin
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully!')
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

# for view login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm( request=request ,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/index/')
                else:
                    messages.error(request, 'Invalid username or password!')
        else:
            form = LoginForm()
        return render(request, 'home/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/index/')


# for view logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#  for dashboard    
def dashboard(request):
    return render(request, 'home/dashboard.html')





