from tabnanny import verbose
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField # importamos RichTextField de ckeditor

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    # content = models.TextField(verbose_name="Contenido")
    # vamos a cambiar el tipo de content, primero se instala ckeditor con pip install ckeditor
    content = RichTextField(verbose_name="Contenido") #usamos RichTextField del ckeditor que ya instalamos
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        
    def __str__(self):
        return self.title