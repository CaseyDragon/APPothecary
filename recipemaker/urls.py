from django.urls import path
from . import views

urlpatterns = [
    path('', views.oils_list, name='oils_list'),
    path('oils/<int:id>', views.oils_detail, name='oils_detail'),
    path('additives/', views.additives_list, name='additives_list'),
    path('additives/<int:id>', views.additives_detail, name='additives_detail'),
    path('volume/', views.volume_calc, name='volume_calc'),
    path('formulas/', views.basic_formulations, name='basic_formulations'),
]
