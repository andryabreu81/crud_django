from ast import Delete
from django.db import models
from requests import delete

class Libro(models.Model):
    id          = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=200,verbose_name='Título')
    imagen      = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    
    # funcion para mejorar como se ven los datos de un registro en el administrador
    def __str__(self):
        fila = 'Titulo: ' + self.titulo + ' - ' + 'Descripcion: ' + self.descripcion
        return fila
    
    # funcion que borra la imagen del storage cuando se elimina el registro de un libro
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()