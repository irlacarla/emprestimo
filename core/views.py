from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
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
    
        return render(request, "central.html")
        
        
        
        
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


def trocarsenha(request):
    if not request.user.is_authenticated():
        return redirect(index)
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context ['form'] = form

    return render (request,"password.html",context)     
    
def cadastrar(request):

    return render(request, "cadastrar.html")      
  
    
