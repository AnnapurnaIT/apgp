from django.contrib import admin
from django.urls import path, include
from . import views

# urls here
urlpatterns = [
    path('',views.homeView, name='dcchome'),
    path('add',views.AddPost, name='addPost'),
]

