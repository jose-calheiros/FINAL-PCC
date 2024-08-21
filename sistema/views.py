from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from turmas.models import Turma, UsuarioTurma
from sistema.form import ExperimentoForm
from sistema.models import Experimento
from usuario.models import Usuario


#FUNÇÃO DE ADICIONAR
@login_required
def add(request, usuarioturma_id):
    turma = get_object_or_404(UsuarioTurma, pk=usuarioturma_id, usuario=request.user)
    
    if request.method == 'POST':
        form = ExperimentoForm(request.POST, request.FILES)
        if form.is_valid():
            experimento = form.save(commit=False)  # Cria a instância sem salvar ainda
            experimento.usuarioturma = turma  # Define a turma associada
            experimento.save()  # Salva o objeto no banco de dados para garantir que tenha um ID


            return redirect('/turma/', pk=turma.id)  # Redireciona para os detalhes da turma
    else:
        form = ExperimentoForm()

    return render(request, 'sistem/add.html', {'form': form, 'turma': turma})

#FUNÇÃO DE LER
@login_required
def read(request,turma_id):
    # Obtém a turma especificada pelo ID
    turma = get_object_or_404(Turma, pk=turma_id)
    
    # Obtém todos os UsuarioTurma associados à turma
    usuarios_turma = UsuarioTurma.objects.filter(turma=turma)
    
    # Obtém todos os Experimentos associados a UsuarioTurma
    experimentos = Experimento.objects.filter(usuarioturma__in=usuarios_turma)
    
    return render(request, 'sistem/lista.html', {'experimentos': experimentos, 'turma': turma})

#FUNÇÃO UPDATE
@login_required
def update(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
   
    if request.method == 'POST':
            form = ExperimentoForm(request.POST, instance=experimento)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/turma/')
            else:
                return render(request, "sistem/update.html", {'form': form, 'id': experimento_id})
    else:
            form = ExperimentoForm(instance=experimento)
            return render(request, "sistem/update.html", {'form': form, 'id': experimento_id})


#FUNCÇOES DE DELETAR
@login_required
def delete(request, experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    if request.user.groups == 'aluno':
        return HttpResponseRedirect('/turma/')
    else:
        experimento.delete()
        return HttpResponseRedirect('/turma/')

@login_required
def confdelete(request,  experimento_id):
    experimento = Experimento.objects.get(pk=experimento_id)
    if request.user.groups == 'aluno':
        return HttpResponse("Apenas professores podem acessar esta página.")
    else:
        return render(request, "sistem/delete.html", {'experimento': experimento})

@login_required
def detail(request, experimento_id):
    experimento = get_object_or_404(Experimento, id=experimento_id)
    turma = experimento.usuarioturma  # Obtém a turma associada ao experimento
    experimentos = turma.experimento_set.all()  # Obtém todos os experimentos associados à turma

    return render(request, 'sistem/detail.html', {'experimento': experimento, 'experimentos': experimentos,  'usuarioturma': turma})

