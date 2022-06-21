from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })


def about(request):

    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })


def register_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    else:
        register_form = RegisterForm()

        if request.method == "POST":
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te haz registrado correctamente!')

                return redirect('/inicio')

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('inicio')
        
    else:
        if request.method == 'POST':
            # se recge el dato username que llegando desde el formulario
            username = request.POST.get('username')
            # se hace lo mismo que con el username, lo que va en comillas es el name que está en el formulario login.html
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            else:
                messages.warning(request, 'No te haz identificado correctamente!')    

        return render(request, 'users/login.html', {
            'title': 'Identificate',
        })

def logout_user(request):
    logout(request)
    return redirect('login')