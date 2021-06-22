from django.shortcuts import redirect, render
from .models import Registro
from .forms import RegistroForm

# Create your views here.
def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def job(request):
    return render (request, 'job.html')

def cotizar(request):
    return render (request, 'sams/cotizar.html')

def iniciosesion(request):
    return render (request, 'iniciosesion.html')

def registrarse(request):
    if request.method=='POST':
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect('index')
    else:
        registro = RegistroForm()

    return render (request, 'sams/registrarse.html', {'registro': registro})