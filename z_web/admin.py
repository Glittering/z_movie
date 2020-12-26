from django.contrib import admin

from z_web.models import *


# Register your models here.

# admin定制
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "up_time"]  # 列表显示字段
    filter_horizontal = ('label',)  # 外键选择


admin.site.register(MovieLabel)  # 注册
admin.site.register(Movie, MovieAdmin)
