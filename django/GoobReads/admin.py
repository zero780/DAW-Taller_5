from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Calificacion)
admin.site.register(Autor)
admin.site.register(Libro_Autor)
