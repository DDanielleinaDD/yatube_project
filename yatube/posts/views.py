from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Group
from django.shortcuts import get_object_or_404


# Create your views here.
# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts':posts}
    return render(request, 'posts/index.html', context)


# Страница с группами
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {'group' : group,
               'posts' : posts,}
    return render(request, 'group/<slug>/', context)