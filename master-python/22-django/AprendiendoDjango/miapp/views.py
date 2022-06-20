from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones(metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio Web con Django | Victor Robles</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>

"""


def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""
    year = 2021
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"
    """
    year = 2021
    hasta = range(year, 2051)

    nombre = 'Victor Robles 2'
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio 2',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

# def interes(request):
#     cantidad = 1000
#     interesA = 0.1
#     cantAnios = 5

#     html = f"Inversión: {cantidad}"
#     html+="""
#         <ul>
#     """
#     for i in range(cantAnios):
#         cantidad *= 1+ interesA
#         html += f"""
#             <li>Año {i+1}:{str(round(cantidad,2))}</li>
#         """
#     html+="""
#         </ul>
#     """
#     return HttpResponse(html)


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Victor", apellidos="Robles")

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,  # propiedad del modelo = valor que llega de la url.., lo llamamos igual para el ejemplo
        content=content,
        public=public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")


def save_article(request):
    ############ METODO POST ###############
    if request.method == 'POST':

        title = request.POST['title']
        if len(title) <= 5:
            return HttpResponse("El titulo es muy pequeño")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title=title,  # propiedad del modelo = valor que llega de la url.., lo llamamos igual para el ejemplo
            content=content,
            public=public
        )

        articulo.save()
        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

    ########### METODO GET ###############
    # if request.method == 'GET':

    #     title = request.GET['title']
    #     if len(title)<=5:
    #         return HttpResponse("El titulo es muy pequeño")

    #     content = request.GET['content']
    #     public = request.GET['public']

    #     articulo = Article(
    #         title=title,  # propiedad del modelo = valor que llega de la url.., lo llamamos igual para el ejemplo
    #         content=content,
    #         public=public
    #     )

    #     articulo.save()
    #     return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    # else:
    #     return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


def create_article(request):

    return render(request, 'create_article.html')



## esta funcion es para el formulario basado en clases
def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']


            ## AQUI USAMOS LE MODELO Article para guardar los datos en la bd
            articulo = Article(
                title=title,  # propiedad del modelo = valor que llega de la url.., lo llamamos igual para el ejemplo
                content=content,
                public=public
            )

            articulo.save()

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el artículo {articulo.id}')
            
            # return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def articulo(request):
    try:
        # muestra el objeto del modelo que tenga titulo "Superman" y public en False
        articulo = Article.objects.get(title="Superman", public=True)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"
    return HttpResponse(response)


def editar_articulo(request, id):

    # el metodo get saca los atributos que elijamos
    articulo = Article.objects.get(pk=id)
    preview_articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"""Articulo editado: <br> 
                                id: {articulo.id}<br/>
                                titulo: {preview_articulo.title}<br/>
                                contenido: {preview_articulo.content}<br/><br/>
                            Nuevos datos:<br/>
                                titulo: <strong>{articulo.title}</strong><br/>
                                contenido: <strong>{articulo.content}</strong>
                        """)


def articulos(request):

    articulos = Article.objects.filter(public=True).order_by('-id')   

    # el metodo all saca todos los atributos del modelo tabla
    # articulos = Article.objects.all().order_by('-id')           # mostrar por id de manera DESCENDENTE
    # articulos = Article.objects.order_by('title')             # order_by para mostrar todo ordenado por el atributo title
    # articulos = Article.objects.order_by('-title')            # order_by para mostrar todo ordenado por el atributo title en REVERSA
    # puede servir para mostrar el ultimo elemento agregado a un carrito
    # articulos = Article.objects.order_by('id')[:3]        # [:3] sirve para limitar la cantidad de elementos, en este caso mostrar solo 3 elementos
    # articulos = Article.objects.order_by('id')[3:7]       # [3:] sirve para mostrar elementos desde el tercero en adelante hasta el septimo

    # articulos = Article.objects.filter(title="Batman", id=3)              # Filtrar por el titulo Batman y el id=3
    # articulos = Article.objects.filter(title__contains = "articulo")      # __contains sirve para mostrar los que contienen dicho texto "articulo", como el like en SQL

    # Lookups
    # articulos = Article.objects.filter(title__exact = "articulo")         # __exact sirve para buscar el elemento con el texto exacto
    # articulos = Article.objects.filter(title__iexact = "articulo")        # __iexact sirve para mostrar los elementos se se llamen articulo, asi sea en mayuscula o minuscula

    # articulos = Article.objects.filter(id__gt=13)                         # mostrar los elementos con id MAYOR que 13
    # articulos = Article.objects.filter(id__gte=13)                        # mostrar los elementos con id MAYOR E IGUAL que 13
    # articulos = Article.objects.filter(id__lt=15)                         # mostrar los elementos con id MENORES A 15
    # articulos = Article.objects.filter(id__lte=15)                        # mostrar los elementos con id MENORES O IGUALES A 15
    # articulos = Article.objects.filter(id__lte=15, title__contains="2")   # mostrar los elementos con id MENORES O IGUALES A 15 y que su titulo contenga "articulo"
    # articulos = Article.objects.filter(
    #                                     title="Articulo"
    #                                 ).exclude( # de la lista que tiene title="Articulo" vamos a excluir los que tienen el public=True
    #                                     public=False
    #                                 )

    # USANDO SQL
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public=0 ")

    # articulos = Article.objects.filter(
    #     Q(title__contains="2") | Q(title__contains="3")   # la Q funciona como un OR, para mostrar los articulos que tengan 2 o 3 en su titulo, la Q se importa al inicio de esta hoja
    # )
    # articulos = Article.objects.filter(
    #     Q(title__contains="2") | Q(public=True)           # la Q funciona como un OR, para mostrar los articulos que tengan 2 o que el public sea True
    # )
    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
