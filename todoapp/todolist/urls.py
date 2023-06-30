from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('log-in/', views.login, name='log-in'),
    path('sign-up/', views.signup, name='sign-up'),
]