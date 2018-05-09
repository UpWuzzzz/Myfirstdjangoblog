from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm, RegisterForm

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
                login(request, user)
                return HttpResponse("登陆成功")
            else:
                return render(request, "Login.html", {'msg': '账号或者密码错误'})
        else:
            return render(request, "Login.html", {'msg': '验证码错误请重输入。'})


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
            if UserProfile.objects.get('username'):
                return render(request, "register.html", {'msg', '用户已经存在',})
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            if UserProfile.objects.get('email'):
                return render(request, "register.html", {'msg', '邮箱已经存在',})
            sex = 'male' if request.POST.get('sex', '') == '1' else 'female'
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.password = make_password(password)
            user_profile.email = email
            user_profile.gender = sex
            user_profile.save()

            # send_register_email(email=email)

            return HttpResponseRedirect('login')
        else:
            return render(request, "register.html", {'msg', '格式输入错误'})


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("登陆成功")
        else:
            return render(request, "login.html", {'msg': '账号或者密码错误'})

    elif request.method == 'GET':
        return render(request, "login.html", {})
