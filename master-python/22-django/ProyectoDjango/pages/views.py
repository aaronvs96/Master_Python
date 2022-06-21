from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login") #primero se importa de decorator, y se agrega login_required para que se muestre esta vista solo si está logueado
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    })