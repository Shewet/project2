from django.urls import path

from . import views


urlpatterns =[
    path('', views.index, name='Travello Index'),
    path('about/', views.about, name='Travello About'),
    path('contact/', views.contact, name='Travello Contact'),
    path('destinations/', views.destinations, name='Travello Destinations'),
    path('elements/', views.elements, name='Travello Elements'),
    path('news/', views.news, name='Travello News'),
    ]