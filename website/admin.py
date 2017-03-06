from django.contrib import admin
from website.models import *


# Register your models here.

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('time', 'content', 'ip')
    search_fields = ('time',)