from django.contrib import admin
from django.urls import path

from z_web.views import *

urlpatterns = [
    path('movies/', movies),  # 第二层url，导向views
]