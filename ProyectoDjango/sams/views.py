from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'sams/index.html')

def about(request):
    return render (request, 'sams/about.html')

def job(request):
    return render (request, 'sams/job.html')

def cotizar(request):
    return render (request, 'sams/cotizar.html')

def iniciosesion(request):
    return render (request, 'sams/iniciosesion.html')

def registrarse(request):
    return render (request, 'sams/registrarse.html')