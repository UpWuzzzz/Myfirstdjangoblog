import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ChangepsdForm

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from utils.email_send import send_register_email


class UserBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        return render(request, "Login.html", {'login_form': login_form, 'hashkey': hashkey, 'image_url': image_url})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("登陆成功")
                else:
                    hashkey = CaptchaStore.generate_key()
                    image_url = captcha_image_url(hashkey)
                    return render(request, "Login.html",
                                  {'msg': '账号未激活', 'hashkey': hashkey, 'image_url': image_url})
            else:
                hashkey = CaptchaStore.generate_key()
                image_url = captcha_image_url(hashkey)
                return render(request, "Login.html", {'msg': '账号或者密码错误', 'hashkey': hashkey, 'image_url': image_url})
        else:
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)
            return render(request, "Login.html", {'login_form': login_form, 'hashkey': hashkey, 'image_url': image_url})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_recodes = EmailVerifyRecord.objects.filter(code=active_code)
        if all_recodes:
            for recode in all_recodes:
                email = recode.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return redirect('/login')
        else:
            HttpResponse('验证码已过期.')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        return render(request, "register.html", {'register_form': register_form, 'hashkey': hashkey, 'image_url': image_url})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('username', '')
            if UserProfile.objects.get(username=username):
                hashkey = CaptchaStore.generate_key()
                image_url = captcha_image_url(hashkey)
                return render(request, "register.html", {'msg': '用户已经存在', 'hashkey': hashkey, 'image_url': image_url})
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            if UserProfile.objects.get(email=email):
                hashkey = CaptchaStore.generate_key()
                image_url = captcha_image_url(hashkey)
                return render(request, "register.html", {'msg': '邮箱已经存在', 'hashkey': hashkey, 'image_url': image_url})
            sex = 'male' if request.POST.get('sex', '') == '1' else 'female'
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.password = make_password(password)
            user_profile.email = email
            user_profile.is_active = False
            user_profile.gender = sex
            user_profile.save()

            send_register_email(email, 'register')

            return redirect('/login')
        else:
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)
            return render(request, "register.html", {'register_form': register_form, 'hashkey': hashkey, 'image_url': image_url})


class ForgetpsdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        render(request, 'forgetpsd.html', {'forget_form': 'forget_form'})

    def post(self, request):
        forget_form = ForgetForm()
        if forget_form.is_valid():
            email = forget_form.Post.get('email', '')
            send_register_email(email, 'forget')
            render(request, '')
        else:
            render(request, 'forgetpsd.html', {'forget_form': 'forget_form'})


# class ChangepsdView(View):
#     def get(self, request):
#         changepsd_form = ChangepsdForm()
#         render(request, 'change_pass.html', {'changepsd_form': changepsd_form})
#
#     def post(self, request):
#         changepsd_form = ChangepsdForm()
#         if changepsd_form.is_valid():
#             old_password = changepsd_form.Post.get('old_password', '')
#             password1 = changepsd_form.Post.get('password1', '')
#             password2 = changepsd_form.Post.get('password2', '')
#             if password1 != password2:
#                 render(request, '')
#             value = Session.objects.get(session_key=request.COOKIES["sessionid"])
#             login_user_id = value.get_decoded()['_auth_user_id']
#             if UserProfile.objects.get(id=login_user_id).password == make_password(old_password):
#
#             render(request, '')
#         else:
#             render(request, 'change_pass.html', {'changepsd_form': changepsd_form})


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("登陆成功")
            else:
                return render(request, "login.html", {'msg': '账号未激活'})
        else:
            return render(request, "login.html", {'msg': '账号或者密码错误'})

    elif request.method == 'GET':
        return render(request, "login.html", {})


def re_captcha(request):
    if request.method == 'GET':
        new_key = CaptchaStore.generate_key()
        to_json_response = {
            'key': new_key,
            'image_url': captcha_image_url(new_key),
        }
        return HttpResponse(json.dumps(to_json_response), content_type='application/json')
    else:
        pass