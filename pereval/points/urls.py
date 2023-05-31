
from django.urls import path
from .views import *

app_name = 'passage'
urlpatterns = [
    path('passage/create/', PassageCreateView.as_view()),
    path('GET/submitData/<int:pk>/', PassageDetailView.as_view()),
    path('photo/create/', PhotoCreateView.as_view()),
    path('coords/create/', CoordsCreateView.as_view()),
    path('users/create/', UsersCreateView.as_view()),
    path('PATCH/submitData/<int:pk>/', PassageUpdateView.as_view()),
]
