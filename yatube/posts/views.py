from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    return HttpResponse('Главная страница Yatube.ru')


# Страница с группами
def group_posts(request, any_slug):
    return HttpResponse(f'Страница группы с постом {any_slug}')