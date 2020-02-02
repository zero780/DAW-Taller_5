from django.db import models

# Create your models here.



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=40)
    nacimiento = models.DateField(null=True, blank=True)
    clave = models.CharField(max_length=40)


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500)
    autores = models.CharField(max_length=500)
    isbn = models.CharField(max_length=40)
    calificacion_promedio = models.CharField(max_length=5, default=0)

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.CharField(max_length=10)

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

class Libro_Autor(models.Model):
    id_libro_autor = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)