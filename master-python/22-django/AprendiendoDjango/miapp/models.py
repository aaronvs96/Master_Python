from tabnanny import verbose
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título") #varchar que tiene un maximo de 100 caracteres
    content = models.TextField(verbose_name="Contenido") #varchar
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to='articles')
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta: # la clase Meta nos permite configurar el modelo (ENTRAR A LA PAGINA ADMIN para visualizar los cambios)
        verbose_name = "Artículo"           # asignar el nombre del modelo en SINGULAR
        verbose_name_plural = "Artículos"   # asignar el nombre del modelo en PLURAL
        ordering = ['id']           #ordenar por id ASCECENDENTE
        ordering = ['-id']          #ordenar por id DESCECENDENTE
        ordering = ['public']       #ordernar por public
        ordering  = ['created_at']  #ordenar del mas viejo al mas nuevo
        ordering = ['-created_at']  #ordenar del mas nuevo al mas viejo
    
    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"

        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_at = models.DateField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"