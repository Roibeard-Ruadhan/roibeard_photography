"""Blog Urls"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name="Intro"),
    path('home/', views.Home, name='Homepage'),
    path('portfolio/', views.Portfolio_1, name='Portfolio_1'),
]