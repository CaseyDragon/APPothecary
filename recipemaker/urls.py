from django.urls import path
from . import views

urlpatterns = [
    path('', views.oils_list, name='oils_list'),
]
