from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article

# Create your views here.
def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html',{
        'title': 'Artículos',
        'articles' : articles
    })

def category(request, category_id):

    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id) #get_object_or_404 sirve para mostrar pantalla de error 404 
    # articles = Article.objects.filter(categories=category)
    
    return render(request, 'categories/category.html', {
        'category': category,
        # 'articles': articles
    })