from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'passage'
urlpatterns = [
    path('passage/create/', PassageCreateView.as_view())
]