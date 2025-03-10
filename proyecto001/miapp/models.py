from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    # auto_now_add me permitirá registrar 
    # la fecha cuando cree el registro
    creado = models.DateTimeField(auto_now_add=True)
    # auto_now me permitirá registrar 
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    # DateField() para guardar la fecha manualmente
    creado = models.DateField()

class Autor(models.Model):
    Sexo_choices=[('M', 'Masculino'),
                   ('F', 'Femenino'),
                   ('O', 'Otro')
                   ]
    nombre =  models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    sexo= models.CharField(max_length=1, choices=Sexo_choices, default="0")
    fech_nacimiento= models.DateField() 
    pais= models.CharField(max_length=30)