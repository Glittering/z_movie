from django.contrib import admin
from django.urls import path

from z_web.views import *

# 第二层url，导向views
urlpatterns = [
    path('movies/', movies),
    path('index/', index),
]