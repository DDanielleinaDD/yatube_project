from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


# Create your views here.
# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts':posts}
    return render(request, 'posts/index.html', context)


# Страница с группами
def group_posts(request):
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = {'title' : title}
    return render(request, template, context)