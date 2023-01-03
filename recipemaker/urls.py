from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('lyecalc/', views.lye_calc, name='lye_calc'),
    path('oils/', views.oils_list, name='oils_list'),
    path('oils/<int:id>', views.oils_detail, name='oils_detail'),
    path('additives/', views.additives_list, name='additives_list'),
    path('additives/<int:id>', views.additives_detail, name='additives_detail'),
    path('myrecipes', views.my_recipes, name='my_recipes'),
    path('volume/', views.volume_calc, name='volume_calc'),
    path('formulas/', views.basic_formulations, name='basic_formulations'),
]
