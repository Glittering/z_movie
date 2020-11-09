from django.contrib import admin
from django.urls import path

from z_web.views import *

urlpatterns = [
    path('movies/', movies),
]