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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetpsdView, re_captcha
from article.views import IndexView, Header, Edit, ArticleView, Rasid, Info, Aside

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('header', Header, name='header'),
    path('edit', Edit, name='header'),
    path('main', ArticleView.as_view(), name='article'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('aside', Aside, name='Aside'),
    path('info', Info, name='info'),
    path('rasid', Rasid, name='rasid'),
    path('login', LoginView.as_view(), name='Login'),
    path('register', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    path('recaptcha/', re_captcha, name='re_captcha'),
    path('active/<str:active_code>', ActiveUserView.as_view(), name='user_active'),
    path('forget', ForgetpsdView.as_view(), name='forget_password'),
]
