from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 留言
class Messages(models.Model):
    content = models.CharField(verbose_name='留言内容', max_length=500, blank=False)
    time = models.DateTimeField(verbose_name='留言时间', auto_now_add=True)
    ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = '留言'

    def __str__(self):
        return '留言'


class SS(models.Model):
    ip = models.GenericIPAddressField(verbose_name='ip地址')
    port = models.CharField(verbose_name='端口', max_length=5, null=False, blank=False)
    region = models.CharField(verbose_name='地区', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'SS'

    def __str__(self):
        return 'SS'
