from  django.urls import path
from . import views
from sanbenito.views import index

urlpatterns = [
    path("", index, name="index"),
]
