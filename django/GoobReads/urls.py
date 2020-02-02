from rest_framework import routers as root
from .views import *
from django.conf.urls import url

# root = root.DefaultRouter()
# root.register(r'mongo',ComidaViewSet)
# urlpatterns=[
#
# ]
# urlpatterns+=root.urls

urlpatterns=[

    url(r'^usuarios/$',UsuariosList.as_view(), name ='usuarios'),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', UsuariosDetail.as_view()),

    url(r'^libros/$', LibroList.as_view(), name='libros'),
    url(r'^libros/(?P<pk>[0-9]+)/$', LibroDetail.as_view()),

    url(r'^calificacion/$', CalificacionList.as_view(), name='calificacion'),
    url(r'^calificacion/(?P<pk>[0-9]+)/$', CalificacionDetail.as_view()),

    url(r'^autores/$', AutorList.as_view(), name='autores'),
    url(r'^autores/(?P<pk>[0-9]+)/$', AutorDetail.as_view()),

    url(r'^libro_autor/$', Libro_AutorList.as_view(), name='libro_autor'),
    url(r'^libro_autor/(?P<pk>[0-9]+)/$', Libro_AutorDetail.as_view()),

]
