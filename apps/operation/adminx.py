__author__ = 'awu'
__date__ = '2018/5/8 9:09'
import xadmin
from xadmin import views

from .models import UserComments, UserFav


class UserCommentsAdmin(object):
    # 后台页面展示数据
    list_display = ['user', 'article', 'comments', 'add_time']
    # 后台搜索数据
    search_fields = ['user', 'article', 'comments']
    # 后台过滤器
    list_filter = ['user', 'article', 'comments', 'add_time']


class UserFavAdmin(object):
    # 后台页面展示数据
    list_display = ['user', 'article', 'add_time']
    # 后台搜索数据
    search_fields = ['user', 'article']
    # 后台过滤器
    list_filter = ['user', 'article', 'add_time']


xadmin.site.register(UserComments, UserCommentsAdmin)
xadmin.site.register(UserFav, UserFavAdmin)
