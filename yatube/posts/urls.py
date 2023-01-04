from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('',views.index, name='main'),
    # Страница с группами
    path('group/<slug:slug>/', views.group_posts, name='groups'),
    # path('groups/', views.group_posts, name='groups')
]
