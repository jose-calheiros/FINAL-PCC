from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from turmas.models import UsuarioTurma
from usuario.models import Usuario
from .forms import UsuarioForms
from rolepermissions.roles import assign_role
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            user = form.save()            
            return redirect('login')
    else:
        form = UsuarioForms()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def update(request, user_id):
    user = Usuario.objects.get(pk=user_id)
   
    if request.method == 'POST':
            form = UsuarioForms(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('usuario/perfil')
            else:
                return render(request, "registration/update.html", {'form': form, 'id': user_id})
    else:
            form = UsuarioForms(instance=user)
            return render(request, "registration/update.html", {'form': form, 'id': user_id})

def perfil(request):
    user_id = request.user.id

    usuarioturma = UsuarioTurma.objects.filter(usuario_id=user_id).latest('data_matricula')

    return render(request, "registration/perfil.html", {'usuarioturma': usuarioturma})
