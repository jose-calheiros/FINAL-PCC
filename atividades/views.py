from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from atividades.models import Atividade
from sistema.models import Experimento
from turmas.models import Turma, UsuarioTurma
from atividades.form import AtividadeForm
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.models import Group

def add_atividade(request, experimento_id):
    experimento = get_object_or_404(Experimento, pk=experimento_id)

    # Obtém o grupo "professor"
    grupo_professores = Group.objects.get(name='professor')
    
    # Obtém o primeiro usuário do grupo
    usuario_professor = grupo_professores.user_set.first()
    
    # Obtém a turma associada a esse professor
    turma_professor = UsuarioTurma.objects.filter(usuario=usuario_professor).first()
    
    # Verifica se a turma foi encontrada
    if turma_professor is None:
        # Trate o caso onde o professor não está associado a nenhuma turma
        return redirect('/error')  # Ajuste a URL conforme necessário
    
    if request.method == 'POST':
        form = AtividadeForm(request.POST, request.FILES)
        if form.is_valid():
            atividade = form.save(commit=False)  # Cria a instância sem salvar ainda
            atividade.experimento = experimento  # Define o experimento associado
            atividade.responsavel = turma_professor  # Define o responsável como a instância de UsuarioTurma
            atividade.save()  # Salva o objeto no banco de dados
            return redirect('/turma', experimento_id=experimento.id)  # Redireciona após salvar
    else:
        form = AtividadeForm()

    return render(request, 'turtem/atividade/add.html', {'form': form, 'experimento': experimento})

@login_required 
def read_atividade(request,experimento_id):
    experimento = get_object_or_404(Experimento, pk=experimento_id)
    atividade = Atividade.objects.filter(experimento = experimento)  # Usando o campo relacionado
    return render(request, 'turtem/atividade/read.html', {'atividades': atividade, 'experimento': experimento})

@login_required
def detail_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    experimento = atividade.experimento  # Obtém a turma associada à atividade
    atividades = experimento.atividades.all()  # Obtém todas as atividades associadas à turma
    return render(request, 'turtem/atividade/detail.html', {'atividade': atividade, 'atividades': atividades, 'experimento': experimento})


@login_required
def delete(request, atividade_id):
    atividade = Atividade.objects.get(pk=atividade_id)
   
    atividade.delete()
    return HttpResponseRedirect('/turma/')
    
@login_required
def confdelete(request,  atividade_id):
    atividade = Atividade.objects.get(pk=atividade_id)
    return render(request, "turtem/atividade/delete.html", {'atividades': atividade})

@login_required
def update(request, atividade_id):
    atividade = Atividade.objects.get(pk=atividade_id)
    if request.method == 'POST':
            form = AtividadeForm(request.POST, instance=atividade)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/turma/')
            else:
                return render(request, "turtem/atividade/update.html", {'form': form, 'id': atividade_id})
    else:
            form = AtividadeForm(instance=atividade)
            return render(request, "turtem/atividade/update.html", {'form': form, 'id': atividade_id})