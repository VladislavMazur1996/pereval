from django.urls import path, re_path
from .views import *

app_name = 'passage'
urlpatterns = [
    path('submitData/create/', PassageCreateView.as_view()),
    path('submitData/<int:pk>/', PassageDetailView.as_view()),
    path('photo/create/', PhotoCreateView.as_view()),
    path('coords/create/', CoordsCreateView.as_view()),
    path('users/create/', UsersCreateView.as_view()),
    path('submitData/<int:pk>/update', PassageUpdateView.as_view()),
    re_path('submitData/(?P<email>.+)/$', PassageListView.as_view()),
]
