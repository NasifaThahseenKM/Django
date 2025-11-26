from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path('add/', views.add_teacher, name='add'),
    path('<str:message>/', views.teacher_list, name='list'),
    
]
