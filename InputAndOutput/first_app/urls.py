from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('add_student/', views.add_student, name = 'add_student'),  
    path('show_student/', views.show_student, name = 'show_student'),  
    path('delete/<int:roll>', views.delete_student, name = 'delete_student'),
]
