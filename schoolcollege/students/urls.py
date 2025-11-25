from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:student_name>/', views.result_page, name='result_page'),
]
