from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('add/', views.add , name= 'add'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('delete-all',views.delete_all, name='delete-all'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('mark-completed/<int:id>',views.markcompleted,name='mark-completed')
]
