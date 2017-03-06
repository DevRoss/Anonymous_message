from django.db import models

# Create your models here.


# 留言
class Messages(models.Model):
    content = models.CharField(verbose_name='留言内容', max_length=500, blank=False)
    time = models.DateTimeField(verbose_name='留言时间', auto_now_add=True)

    # ip = models.GenericIPAddressField()
    class Meta:
        verbose_name = verbose_name_plural = '留言'

    def __str__(self):
        return '留言'
