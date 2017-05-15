from django.db import models
from django.contrib.auth.models import User
import os
from Anonymous_message.settings import MEDIA_ROOT


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
    server_name = models.CharField(verbose_name='服务器名', max_length=20, null=False, blank=False)
    ip = models.GenericIPAddressField(verbose_name='ip地址')
    port = models.CharField(verbose_name='远程端口', max_length=5, null=False, blank=False)
    region = models.CharField(verbose_name='地区', max_length=20, null=True, blank=True)
    password = models.CharField(verbose_name='密码', max_length=30, null=False, blank=False)
    encrypt_method = models.CharField(verbose_name='加密方式', max_length=30, null=False, blank=False)
    qr_code = models.FilePathField(verbose_name='QC路径', path=os.path.join(MEDIA_ROOT, 'QR'), match='*\.png$',
                                   recursive=True, max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = 'SS'

    def __str__(self):
        return 'SS'
