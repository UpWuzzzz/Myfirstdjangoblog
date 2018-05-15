from datetime import datetime
from django.db import models
from users.models import UserProfile
from article.models import Post


# Create your models here.
class UserComments(models.Model):
    """
        用户评论
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    article = models.ForeignKey(Post, verbose_name='文章', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name


class UserFav(models.Model):
    """
        用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    article = models.IntegerField(default=0, verbose_name='文章编号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserPraise(models.Model):
    """
        用户点赞
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    article = models.IntegerField(default=0, verbose_name='文章编号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u"用户点赞"
        verbose_name_plural = verbose_name

