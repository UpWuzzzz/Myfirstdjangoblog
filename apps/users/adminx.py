__author__ = 'awu'
__date__ = '2018/5/8 9:09'
import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyRecord


class BaseSetting(object):
    """
        添加全局变量，改成自己喜欢的格式
    """
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '博客'
    site_footer = '博客'
    # 菜单的折叠方式
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    # 后台页面展示数据
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 后台搜索数据
    search_fields = ['code', 'email', 'send_type']
    # 后台过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)