from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug') #seleccionamos esos 3 datos del modelo
    
    return {
        'pages': pages
    }