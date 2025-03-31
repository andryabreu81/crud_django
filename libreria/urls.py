from django.urls import path
from . import views

# archivo de configuracion settings.py
from django.conf import settings
from django.contrib.staticfiles.urls import static

# ruta que invoca la vista o funcion de nombre inicio en views.py
urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('libros/',views.libros, name='libros'), # lista de libros
    path('libros/crear/',views.crear, name='crear'), # crear libro
    #path('libros/editar/',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'), # eliminar libro
    path('libros/editar/<int:id>',views.editar, name='editar'), # editar libro
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)