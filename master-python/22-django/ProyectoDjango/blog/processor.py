from blog.models import Category, Article

def get_categories(request):

    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name') #seleccionamos esos 2 datos del modelo
    
    return {
        'categories': categories,
        'ids': categories_in_use
    }

def get_articles(request):

    articles_in_use = Article.objects.filter(public=True).values_list('id','title')

    return {
        'articles_in_use': articles_in_use
    }