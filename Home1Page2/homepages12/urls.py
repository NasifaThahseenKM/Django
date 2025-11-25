from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home2/', views.home2, name='home2'),
    path('about2/', views.about2, name='about2'),
    path('contact2/', views.contact2, name='contact2'),
]
