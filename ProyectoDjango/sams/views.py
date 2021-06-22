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

def registrarse_ver(request):
    registro = Registro.objects.all()

    return render(request, 'sams/registrarse_ver.html', context={'registro':registro})

def registrarse_modificar(request,id):
    registro = Registro.objects.get(rutRegistro=id)
    datos = {
        'form': RegistroForm(instance=registro)
    }
    if request.method=='POST':
        formulario = RegistroForm(data=request.POST, instance = registro)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver-registro')

    return render(request, 'sams/registrarse_modificar.html', datos)