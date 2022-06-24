"""Blog Urls"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name="index"),
    path('home/', views.Home, name='home'),
    path('portfolio/', views.Portfolio_1, name='portfolio'),
]