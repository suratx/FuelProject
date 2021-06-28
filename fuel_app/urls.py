from django.urls import path
from django.contrib.auth import views as auth_views

# from fuel_app import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
    path('quote', views.quote, name='quote'),
    path('history', views.history, name='history'),
    path('profile', views.profile, name='profile')
]