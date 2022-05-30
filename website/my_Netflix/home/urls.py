from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]



