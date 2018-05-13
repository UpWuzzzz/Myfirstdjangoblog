from django.shortcuts import render,render_to_response
from django.views.generic.base import View

from .models import Post
from users.models import UserProfile


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render_to_response('blogs.html')


def Header(request):
    return render_to_response('header.html')


def Edit(request):
    return render_to_response('edit.html')


class ArticleView(View):
    def get(self, request, user_id):
        if user_id == '0':
            article_list = Post.objects.all().order_by('-create_time')
        else:
            article_list = Post.objects.filter(author_id=user_id).order_by('-create_time')
        return render(request, 'main.html', {'article_list': article_list})


def Aside(request):
    return render_to_response('aside.html')


def Info(request):
    return render_to_response('info.html')


def Rasid(request):
    return render_to_response('rasid.html')
