from django.urls import path
from . import views

app_name = 'heroes'

urlpatterns = [
    path('', views.heroes_index, name='index'),
    path('<int:pk>/', views.hero_detail, name='detail'),
]

