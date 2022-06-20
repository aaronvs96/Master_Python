from django.contrib import admin
from .models import Article, Category # primero debemos importar los modelos

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # mostrar la fecha de creacion  modificacion

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel
title = "Master en Python - Víctor Robles"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión"