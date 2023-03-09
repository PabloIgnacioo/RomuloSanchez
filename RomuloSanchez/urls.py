from django.urls import path

from InterfazPrincipal.views import Inicio,Nosotros,Proyectos,Galeria,Contactos,posts
urlpatterns = [
    path('',Inicio, name='Inicio'),
    path('nosotros',Nosotros , name='Nosotros'),
    path('proyecto',Proyectos , name='Proyectos'),
    path('galeria',Galeria , name='Galeria'),
    path('contactos',Contactos , name='Contactos'),
    path('post/<int:id>',posts, name="posts"),
]