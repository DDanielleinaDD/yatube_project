from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('',views.index),
    # Страница с группами
    path('group/<slug:any_slug>/', views.group_posts),
]