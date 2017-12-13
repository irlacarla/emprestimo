from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from .models import CadastrarObjeto
from .forms import Notasforms

from django.contrib.auth import login


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): #verificar se é válido
            login(request, form.get_user())
            return redirect(central)
            
        else:
            return render(request, "index.html", {"form": form })
            
    return render(request, "index.html", {"form": AuthenticationForm()})       
    
    
    
def central(request):
    lista_notas = CadastrarObjeto.objects.all().order_by('nome') 
    return render(request, 'central.html', {'notas': lista_notas}) 
        
        
def criar_usuario(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()

    return render(request, "criar_usuario.html", {"form": form})
        
        
        
        
def perfil(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso nao esteja logado
        return redirect(index)
     return render(request,"perfil.html")        
        
        
        
def editar (request):
    if not request.user.is_authenticated():
        return redirect(index)

    context = {}
    if request.method == 'POST':
        form = EditPerfilForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()

            context['success'] = True
    else:
        form = EditPerfilForm(instance=request.user)
    context['form'] = form

    return render (request,"editar.html",context)   


def passwordReset(request):
    """ Sets a new password for the user (without needing to know the old
    password)
    """
    
    form = SetPasswordForm(user=request.user, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            form = SetPasswordForm(user=request.user)

    return render(request, "reset.html", {"form": form})

def indexx(request):
	lista_notas = Nota.objects.all().order_by('nome') 
	return render(request, 'central.html', {'notas': lista_notas}) 



def detalhes_objeto(request,pk):
    nota = CadastrarObjeto.objects.get(id=pk)
    return render(request, 'detalhes.html', {'detalhes': nota})
    
    
def criar_objetos(request):
    form = Notasforms(request.POST or None)
    if request.method == 'POST':
        form = Notasforms(request.POST) 
        form = form.save()
        form = Notasforms()
        
    return render(request, 'criarobj.html', {'form': form}) 
    
       
   
  
    
