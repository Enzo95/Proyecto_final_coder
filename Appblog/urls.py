from django.urls import path
from Appblog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
#    path('recetaFormulario/', views.cursoFormulario, name = "cursoFormulario"),
#    path('busquedaReceta/', views.busquedaCamada, name = "busquedaCamada"),
    path('receta/list', views.RecetaList.as_view(), name='Lista Receta'),
    path('acerca_de_nosotros', views.acerca_nuestro, name='Acerca nosotros'),
    path(r'^(?P<pk>\d+)$', views.RecetaDetalle.as_view(), name='Detalle Receta'),
    path(r'^nuevo$', views.RecetaCreacion.as_view(),name= 'Nueva Receta'),
    path(r'^editar/(?P<pk>\d+)$', views.RecetaUpdate.as_view(),name= 'Editar Receta'),
    path(r'^borrar/(?P<pk>\d+)$', views.RecetaDelete.as_view(), name='Eliminar Receta'),
]