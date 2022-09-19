from django.shortcuts import render
from Appblog.models import *
from django.views.generic import ListView, detail, edit

# Create your views here.
def inicio(request):

    return render(request,"Appblog/inicio.html")

class RecetaList(ListView):

    model = Receta
    template_name= "Appblog/receta_list.html"

class RecetaDetalle(detail.DetailView):

    model = Receta
    template_name= "Appblog/receta_detalle.html"

class RecetaCreacion(edit.CreateView):

    model = Receta
    success_url= "/Appblog/receta/list"
    fields = ['nombre','tipo','ingredientes','procedimiento']

class RecetaUpdate(edit.UpdateView):

    model = Receta
    success_url= "/Appblog/receta/list"
    fields = ['nombre','tipo','ingredientes','procedimiento']

class RecetaDelete(edit.DeleteView):

    model = Receta
    success_url= "/Appblog/receta/list"

def acerca_nuestro(request):

    return render(request,"Appblog/acercaNuestro.html")
