from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario
from .forms import TurmaCodigoForm, TurmaForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from turmas.models import Turma, UsuarioTurma
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.models import Group


#CRIAR TURMAS
@has_role_decorator('professor')
@login_required
def add_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            turma = form.save()
            return redirect('/turma')  # Redireciona após salvar
    else:
        form = TurmaForm()  # Cria um novo formulário vazio
    return render(request, 'turtem/add.html', {'form': form})


#LER AS TURMAS CRIADAS

@login_required
def read(request):
    usuario = request.user
    turmas = Turma.objects.filter(matricula=usuario)  # Usando o campo relacionado 
    return render(request, 'turtem/lista.html', {'turmas': turmas})
    
#FUNCÇOES DE DELETAR
@has_role_decorator('professor')
@login_required
def delete(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
    turma.delete()
    return HttpResponseRedirect('/turma/')

@has_role_decorator('professor')
@login_required
def confdelete(request,  turma_id):
    turma = Turma.objects.get(pk=turma_id)
    return render(request, "turtem/delete.html", {'turma': turma})


#EDITAR/ATUALIZAR
@has_role_decorator('professor')
@login_required
def update(request, turma_id):
    turma = Turma.objects.get(pk=turma_id)
   
    if request.method == 'POST':
            form = TurmaForm(request.POST, instance=turma)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('detail', turma_id=turma.id)
            else:
                return render(request, "turtem/update.html", {'form': form, 'id': turma_id})
    else:
            form = TurmaForm(instance=turma)
            return render(request, "turtem/update.html", {'form': form, 'id': turma_id})
        

#DETALHES TURMAS
def detail(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    # Recupera o UsuarioTurma relacionado ao usuário logado e à turma especificada
    usuario_turma = UsuarioTurma.objects.filter(usuario=request.user, turma=turma).first()
    usuarios = buscar_usuarios_grupo_em_turma(turma_id)

    return render(request, 'turtem/detail.html', {'turma': turma, 'usuario_turma': usuario_turma, 'usuarios': usuarios})

@login_required
def entrar_turma(request):
    if request.method == 'POST':
        form = TurmaCodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            
            # Tenta encontrar a turma com o código fornecido
            turma = get_object_or_404(Turma, codigo=codigo)
            usuario = Usuario.objects.get(pk=request.user.pk)  # Obtém uma instância do modelo Usuario

            # Adiciona o usuário à turma se ele ainda não estiver associado
            if request.user not in turma.matricula.all():
                turma.matricula.add(usuario)  # Adiciona o usuário à turma
                messages.success(request, "Você entrou na turma com sucesso.")
            else:
                messages.info(request, "Você já está inscrito nesta turma.")
            
            return redirect('/turma/')  # Redireciona para a página de turmas
    else:
        form = TurmaCodigoForm()
    
    return render(request, 'turtem/entrar.html', {'form': form})


def buscar_usuarios_grupo_em_turma(turma_id, grupo_nome='aluno'):
    # Primeiro, recuperamos o grupo 'Aluno'
    grupo = Group.objects.get(name=grupo_nome)

    # Em seguida, filtramos os usuários que estão neste grupo   
    usuarios_no_grupo = Usuario.objects.filter(groups=grupo)

    # Agora, filtramos esses usuários que estão associados a uma turma específica
    usuarios_na_turma = usuarios_no_grupo.filter(usuarioturma__turma_id=turma_id).distinct()

    return usuarios_na_turma

