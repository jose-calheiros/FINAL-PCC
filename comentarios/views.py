from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from usuario.models import Usuario
from comentarios.models import Comentarios
from atividades.models import Atividade
from comentarios.form import ComentariosForm
from django.contrib.auth.decorators import login_required


def read_comentario(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    usuario = get_object_or_404(Usuario, pk=request.user.pk)

    if request.method == 'POST':
        form = ComentariosForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.atividade = atividade
            comentario.usuario = usuario
            comentario.save()

            # Redireciona para evitar que o formulário seja re-submetido ao atualizar a página
            return redirect('read_comentario', atividade_id=atividade.id)
    else:
        form = ComentariosForm()

    comentarios = Comentarios.objects.filter(atividade=atividade).order_by('-data')

    return render(request, 'turtem/comentarios/read.html', {
        'form': form,
        'comentarios': comentarios,
        'atividade': atividade,
        'usuario': usuario
    })
@login_required 
def update_comentario(request,comentario_id):
   
    comentario = Comentarios.objects.get(pk=comentario_id)
    if request.method == 'POST':
            form = ComentariosForm(request.POST, instance=comentario)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/turma/')
            else:
                return render(request, "sistem/update.html", {'form': form, 'id': comentario_id})
    else:
            form = ComentariosForm(instance=comentario)
            return render(request, "turtem/comentarios/update.html", {'form': form, 'id': comentario_id})


@login_required 
def delete_comentario(request, comentario_id):
    # Obtém o comentário com base no ID fornecido
    comentario = get_object_or_404(Comentarios, pk=comentario_id)
    usuario = Usuario.objects.get(pk=request.user.pk)

    # Verifica se o usuário que está tentando excluir é o mesmo que criou o comentário
    if Comentarios.objects.filter(usuario=usuario):
        comentario.delete()  # Exclui o comentário
    else:
        
    
        return redirect('/turma/')  # Redireciona para a página de turmas ou outra página apropriada