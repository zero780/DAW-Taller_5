# Generated by Django 2.2.3 on 2019-08-24 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GoobReads', '0007_auto_20190824_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=500)),
                ('autores', models.CharField(default='', max_length=500)),
                ('isbn', models.CharField(max_length=40)),
                ('calificacion_promedio', models.CharField(default=0, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=40)),
                ('nacimiento', models.DateField(blank=True, null=True)),
                ('clave', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Libro_Autor',
            fields=[
                ('id_libro_autor', models.AutoField(primary_key=True, serialize=False)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoobReads.Autor')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoobReads.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.CharField(max_length=10)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoobReads.Libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoobReads.Usuario')),
            ],
        ),
    ]
