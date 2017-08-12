from django.contrib import admin
from website.models import *


# Register your models here.

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('time', 'content', 'ip')
    search_fields = ('time',)


@admin.register(SS)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'ip', 'port', 'password', 'region', 'encrypt_method')
    search_fields = ('region',)

@admin.register(PageShot)
class PageShotAdmin(admin.ModelAdmin):
    list_display = ('shot_name', 'url', 'file_path')

