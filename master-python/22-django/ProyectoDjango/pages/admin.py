from django.contrib import admin
from .models import Page # importamos el archivo models con nuestro modelo

# Register your models here.
admin.site.register(Page) # registramos nuestro modelo

#Configuracion del panel:
title = "Proyecto con Django"
subtitle = "Panel de gestión"

admin.site.site_header = title # cambiamos el titulo de la pagina
admin.site.site_title = title #cambiamos el titulo que sale en la pestaña del navegador
admin.site.index_title = subtitle # cambiamos el nombre al Sitio Administrativo