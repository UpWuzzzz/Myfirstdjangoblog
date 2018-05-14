from django.shortcuts import render,render_to_response
from django.views.generic.base import View

from .models import Post
from users.models import UserProfile
from django.contrib.sessions.models import Session


# Create your views here.
class IndexView(View):
    def get(self, request):
        value = Session.objects.get(session_key=request.COOKIES["sessionid"])
        login_user_id = value.get_decoded()['_auth_user_id']
        login_user = UserProfile.objects.get(id=login_user_id).username
        return render(request, 'blogs.html', {'login_user': login_user, 'login_user_id': login_user_id})


def Header(request, login_user):
    return render(request, 'header.html', {'login_user': login_user})


def Edit(request, user_id):
    return render(request, 'edit.html', {'login_user_id': user_id})


class ArticleView(View):
    def get(self, request, user_id):
        value = Session.objects.get(session_key=request.COOKIES["sessionid"])
        login_user_id = value.get_decoded()['_auth_user_id']
        login_user = UserProfile.objects.get(id=login_user_id).username
        if user_id == 'fontpage':
            article_list = Post.objects.all().order_by('-create_time')
        else:
            article_list = Post.objects.filter(author_id=user_id).order_by('-create_time')
        return render(request, 'main.html', {'article_list': article_list, 'login_user': login_user})


def Aside(request, user_id):
    return render(request, 'aside.html', {'login_user_id': user_id})


def Info(request, user_id):
    return render(request, 'info.html', {'login_user_id': user_id})


def Rasid(request):
    return render(request, 'rasid.html')
