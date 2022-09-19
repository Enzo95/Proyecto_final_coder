from django.shortcuts import render
from Appblog.models import *
from django.views.generic import ListView, detail, edit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from Appblog.forms import UserRegisterForm

@login_required
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

@login_required
def acerca_nuestro(request):

    return render(request,"Appblog/acercaNuestro.html")

def login_request(request):
    
    if request.method =="POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                return render(request,"Appblog/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, "Appblog/inicio.html", {"mensaje": "Error, datos incorrectos"})
        
        else:
            return render(request, "Appblog/login.html", {'form':form})

    form = AuthenticationForm()
    
    return render(request, "Appblog/login.html",{'form':form})

def register(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"Appblog/inicio.html",{"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request,"Appblog/registro.html", {"form":form})