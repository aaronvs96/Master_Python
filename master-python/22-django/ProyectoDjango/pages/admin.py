from django.contrib import admin
from .models import Page # importamos el archivo models con nuestro modelo

#Configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') # esto agrega buscador en el administrador de pages
    list_filter = ('visible',) #muestra filtro por paginas visibles o no visibles
    list_display = ('title', 'visible', 'created_at') # agrega columnas del titulo, visible y fecha de creacion
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin) # registramos nuestro modelo

#Configuracion del panel:
title = "Proyecto con Django"
subtitle = "Panel de gestión"

admin.site.site_header = title # cambiamos el titulo de la pagina
admin.site.site_title = title #cambiamos el titulo que sale en la pestaña del navegador
admin.site.index_title = subtitle # cambiamos el nombre al Sitio Administrativo