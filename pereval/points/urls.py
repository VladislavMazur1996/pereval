from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'passage'
urlpatterns = [
    path('passage/create/', PassageCreateView.as_view()),
    path('all/', PassageListView.as_view()),
    path('GET/submitData/<int:pk>/', PassageDetailView.as_view()),
    path('photo/create/', PhotoCreateView.as_view()),
    path('coords/create/', CoordsCreateView.as_view()),
    path('users/create/', UsersCreateView.as_view()),
]
