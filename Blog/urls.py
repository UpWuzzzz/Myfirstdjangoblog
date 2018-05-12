"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetpsdView, re_captcha

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('', , name='index'),
    path('login', LoginView.as_view(), name='Login'),
    path('register', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    path('recaptcha/', re_captcha, name='re_captcha'),
    path('active/<str:active_code>', ActiveUserView.as_view(), name='user_active'),
    path('forget', ForgetpsdView.as_view(), name='forget_password'),
]
