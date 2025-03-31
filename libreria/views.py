from django.shortcuts import render, redirect
from django.http import HttpResponse

# formularios
from .forms import LibroForm

# modelos
from .models import Libro

# Create your views here.

# funcion que responde un mensaje en html
def inicio(request): 
    #return HttpResponse("<h1>Bienvenido Develoteca</h1>")
    return render(request,'paginas/inicio.html')

# funcion que retorna a la vista nosotros.html
def nosotros(request):
    return render(request,'paginas/nosotros.html')

# funcion que retorna a la lista de libros
def libros(request):
    libros = Libro.objects.all()
    # print(libros)
    return render(request,'libros/index.html',{'libros': libros})

# funcion que retorna a la vista de crear libro
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('libros') #redireciona a esa ruta

    return render(request,'libros/crear.html', {'formulario': formulario})

# funcion que retorna a la vista de editar libro
def editar(request, id):
    libro      = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros') #redireciona a esa ruta

    return render(request,'libros/editar.html', {'formulario':formulario})

# funcion que elimina un libro y retorna a la vista de libros
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()

    return redirect('libros') #redireciona a esa ruta