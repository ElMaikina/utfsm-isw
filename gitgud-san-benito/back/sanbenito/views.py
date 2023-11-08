from pyclbr import Class
from wsgiref import validate
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver
from django.apps import apps

from . serializer import *
from . models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model, login ,logout
from rest_framework import permissions, status


# Usa el API REST para conectarse con React

# Muestra todos los carabineros
class Carabineros(ModelViewSet):
    queryset = Carabinero.objects.all()
    serializer_class = CarabineroSerial

# Muestra todos los inspectores
class Inspectores(ModelViewSet):
    queryset = Inspector.objects.all()
    serializer_class = InspectorSerial

# Muestra todos los infractores
class Infractores(ModelViewSet):
    queryset = Infractor.objects.all()
    serializer_class = InfractorSerial

# Muestra todos las infracciones
class Infracciones(ModelViewSet):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerial

# Muestra todos las infracciones
class Evidencias(ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerial
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        clean_data = custom_validation(request.data)
        serializer = SerieUsuarioR(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    permission_classes = permission_classes = (permissions.AllowAny,)
    authenthication_classes = (SessionAuthentication,)

    def post(self,request):
        data = request.data
        assert validate_mail(data)
        assert validate_password(data)
        serializer = SerieUsuarioL(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request,user)
            return Response(serializer.data,status=status.HTTP_200_OK)
class UserLogout(APIView):
    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authenthication_classes = (SessionAuthentication)
    def get(self,request):
        serializer = SerieUsuario(request.user)
        return Response({'user':serializer.data},status=status.HTTP_200_OK)
    
