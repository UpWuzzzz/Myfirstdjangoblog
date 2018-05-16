import json
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.base import View

from .models import Post
from users.models import UserProfile
from operation.models import UserFav, UserPraise
from django.contrib.sessions.models import Session
from django.http import HttpResponse


# Create your views here.
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            value = Session.objects.get(session_key=request.COOKIES["sessionid"])
            login_user_id = value.get_decoded()['_auth_user_id']
            login_user = UserProfile.objects.get(id=login_user_id).username
        else:
            login_user_id = -1
            login_user = '未登录'
        return render(request, 'blogs.html', {'login_user': login_user, 'login_user_id': login_user_id})


def Header(request, login_user):
    return render(request, 'header.html', {'login_user': login_user})


def Edit(request, user_id):
    if user_id == '-1':
        return redirect('/login')
    return render(request, 'edit.html', {'login_user_id': user_id})


class ArticleView(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            value = Session.objects.get(session_key=request.COOKIES["sessionid"])
            login_user_id = value.get_decoded()['_auth_user_id']
            login_user = UserProfile.objects.get(id=login_user_id).username
            has_fav = UserFav.objects.filter(user_id=request.user)
            hav_praise = UserPraise.objects.filter(user_id=request.user)
            if user_id == 'fontpage':
                article_list = Post.objects.all().order_by('-create_time')
            else:
                article_list = Post.objects.filter(author_id=user_id).order_by('-create_time')
            return render(request, 'main.html',
                          {'article_list': article_list, 'has_fav': has_fav, 'hav_praise': hav_praise})
        else:
            if user_id == 'fontpage':
                article_list = Post.objects.all().order_by('-create_time')
                return render(request, 'main.html', {'article_list': article_list})
            else:
                return redirect('/login')


def Aside(request, user_id):
    return render(request, 'aside.html', {'login_user_id': user_id})


def Info(request, user_id):
    if user_id == '-1':
        return redirect('/login')
    return render(request, 'info.html', {'login_user_id': user_id})


def Rasid(request):
    return render(request, 'rasid.html')


class AddFavView(View):
    """
        用户收藏
    """
    def post(self, request):
        article_id = request.POST.get('article', '')

        if not request.user.is_authenticated:
            data = {
                'status': 'fail',
                'msg': '用户未登录',
            }
            return HttpResponse(json.dumps(data), content_type='application/json')

        exist_recodes = UserFav.objects.filter(user=request.user, article=article_id)
        if exist_recodes:
            exist_recodes.delete()

            article = Post.objects.get(id=article_id)
            article.fav_num -= 1
            nums = article.fav_num
            article.save()
            dic = {
                'status': 'success',
                'msg': '取消收藏成功',
                'fav_num': nums,
            }
            return HttpResponse(json.dumps(dic),
                                content_type='application/json')
        else:
            user_fav = UserFav()
            user_fav.user = request.user
            user_fav.article = article_id
            user_fav.save()

            article = Post.objects.get(id=article_id)
            article.fav_num += 1
            nums = article.fav_num
            article.save()
            dic ={
                'status': 'success',
                'msg': '收藏成功',
                'fav_num': nums,
            }
            return HttpResponse(json.dumps(dic),
                                content_type='application/json')


class AddPraiseView(View):
    def post(self, request):
        article_id = request.POST.get('article', '')

        if not request.user.is_authenticated:
            data = {
                'status': 'fail',
                'msg': '用户未登录',
            }
            return HttpResponse(json.dumps(data), content_type='application/json')

        exist_recodes = UserPraise.objects.filter(user=request.user, article=article_id)
        if exist_recodes:
            exist_recodes.delete()

            article = Post.objects.get(id=article_id)
            article.praise_num -= 1
            nums = article.praise_num
            article.save()
            dic = {
                'status': 'success',
                'msg': '取消收藏成功',
                'praise_num': nums,
            }
            return HttpResponse(json.dumps(dic),
                                content_type='application/json')
        else:
            user_Praise = UserPraise()
            user_Praise.user = request.user
            user_Praise.article = article_id
            user_Praise.save()

            article = Post.objects.get(id=article_id)
            article.praise_num += 1
            nums = article.praise_num
            article.save()
            dic = {
                'status': 'success',
                'msg': '收藏成功',
                'praise_num': nums,
            }
            return HttpResponse(json.dumps(dic),
                                content_type='application/json')