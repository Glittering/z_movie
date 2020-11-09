from django.contrib import admin

from z_web.models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "up_time"]
    filter_horizontal = ('label',)

admin.site.register(MovieLabel)
admin.site.register(Movie, MovieAdmin)