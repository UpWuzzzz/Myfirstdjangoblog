from datetime import datetime
from django.db import models
from users.models import UserProfile


# Create your models here.
class Tag(models.Model):
    """
        创建标签数据表
    """
    name = models.CharField(max_length=20, verbose_name='标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='建立时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """
        创建文章数据表模型
    """
    title = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章内容')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='文章创建时间')
    modified_time = models.DateTimeField(default=datetime.now, verbose_name='文章修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='文章摘要')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    praise_num = models.IntegerField(default=0, verbose_name='点赞数')


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
