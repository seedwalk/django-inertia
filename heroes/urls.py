from django.urls import path
from . import views

app_name = 'heroes'

urlpatterns = [
    path('', views.heroes_index, name='index'),
    path('villains/', views.villains_index, name='villains'),
    path('<int:pk>/', views.hero_detail, name='detail'),
]

