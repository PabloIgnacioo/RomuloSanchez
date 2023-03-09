from django.shortcuts import render
from .models import contacto,Post
from .forms import contacto_form

# Create your views here.


def Inicio(request):
    return render(request, 'InterfazPrincipal/Inicio.html')


def Nosotros(request):
    return render(request,'InterfazPrincipal/nosotros.html')

def Proyectos(request):
    return render(request,'InterfazPrincipal/proyectos.html')
    
def Galeria(request):
    posts = Post.objects.all()
    return render(request,'InterfazPrincipal/Galerias.html', {"posts": posts})

def Contactos(request):
    data = {
        'form':contacto_form
    }
    if request.method == 'POST':
        formulario = contacto_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario
    return render(request,'InterfazPrincipal/contactos.html', data)

def posts(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'InterfazPrincipal/posts.html', {"posts": posts})
