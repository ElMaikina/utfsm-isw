from django.contrib import admin
from django.urls import path, include
from . import views
from sanbenito.views import index
from .models import *

urlpatterns = [
    path('admin/', admin.site.urls)
]
