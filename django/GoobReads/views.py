from .serializer import *
from rest_framework import viewsets as view
from .models import *
from rest_framework import generics
from django.shortcuts import get_object_or_404


# Create your views here.

#API REST
#get, post
class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


#get, post
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer



#get, post
class CalificacionList(generics.ListCreateAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class CalificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer


#get, post
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


#get, post
class Libro_AutorList(generics.ListCreateAPIView):
    queryset = Libro_Autor.objects.all()
    serializer_class = Libro_AutorSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )

        return obj

#updtate, delete
class Libro_AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro_Autor.objects.all()
    serializer_class = Libro_AutorSerializer