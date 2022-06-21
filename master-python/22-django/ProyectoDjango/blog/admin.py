from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) #agregarlo siempre una coma cuando solo agregaras un atributo, python debe interpretar que esto es una tupla, por eso se agrega la coma
    list_display = ('name', 'created_at') # agrega columnas del nombre y fecha de creacion
    search_fields = ('name', 'description') # esto agrega buscador en el administrador de categorias

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)