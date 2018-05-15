__author__ = 'awu'
__date__ = '2018/5/14 15:30'

from django.urls import path
from .views import IndexView, Header, Edit, ArticleView, Rasid, Info, Aside, AddFavView, AddPraiseView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('header/<str:login_user>', Header, name='header'),
    path('edit/<str:user_id>', Edit, name='edit'),
    path('main/<str:user_id>', ArticleView.as_view(), name='main'),
    path('info/<str:user_id>', Info, name='info'),
    path('aside/<str:user_id>', Aside, name='aside'),
    path('rasid', Rasid, name='rasid'),
    # 用户收藏
    path('add_fav/', AddFavView.as_view(), name='add_fav'),
    # 用户点赞
    path('add_praise/', AddPraiseView.as_view(), name='add_praise')
]