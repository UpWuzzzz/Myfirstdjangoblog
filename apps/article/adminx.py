__author__ = 'awu'
__date__ = '2018/5/12 14:46'
from .models import Post, Tag
import xadmin


class TagsAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class PostAdmin(object):
    list_display = ['title', 'body', 'author', 'tags', 'create_time', 'modified_time']
    search_fields = ['title', 'body', 'author', 'tags']
    list_filter = ['title', 'body', 'author', 'tags', 'create_time', 'modified_time']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagsAdmin)

