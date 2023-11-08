from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .models import *
from .views import *

post_router = DefaultRouter()
post_router.register(r'carabineros', Carabineros)
post_router.register(r'inspectores', Inspectores)
post_router.register(r'infractores', Infractores)
post_router.register(r'infracciones', Infracciones)
post_router.register(r'evidencia', Evidencias)


urlpatterns = [
    path('register', UserRegister.as_view(), name = 'register'),
    path('login', UserLogin.as_view(), name = 'login'),
    path('logout', UserLogout.as_view(), name = 'logout'),
    path('user', UserView.as_view(), name = 'user'),


]