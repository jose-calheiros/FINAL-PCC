from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from bate_papo.form import Bate_papoForm
from bate_papo.models import Bate_papo
from turmas.models import Turma, UsuarioTurma


def read_batepapo(request, turma_id):
    turma = get_object_or_404(Turma, pk=turma_id)
    usuarios_turma = UsuarioTurma.objects.filter(turma=turma)
    bate_papo = Bate_papo.objects.filter(usuarioturma__in=usuarios_turma).order_by('-data')

    # Lidar com o envio do formulário
    if request.method == 'POST':
        form = Bate_papoForm(request.POST, request.FILES)
        if form.is_valid():
            mensagem = form.save(commit=False)
            # Obtém o UsuarioTurma do usuário logado
            usuarioturma = get_object_or_404(UsuarioTurma, usuario=request.user, turma=turma)
            mensagem.usuarioturma = usuarioturma
            mensagem.save()
            return redirect('read_batepapo', turma_id=turma.id)  # Redireciona para a mesma página após o envio
    else:
        form = Bate_papoForm()

    return render(request, 'turtem/batepapo/read.html', {
        'bate_papo': bate_papo,
        'turma': turma,
        'form': form
    })


@login_required
def update_batepapo(request, mensagem_id):
    # Obtém a instância do objeto Bate_papo correspondente ao ID fornecido
    batepapo = get_object_or_404(Bate_papo, pk=mensagem_id)

    if request.method == 'POST':
        form = Bate_papoForm(request.POST, instance=batepapo)
        if form.is_valid():
            form.save()
            return redirect('read_batepapo', turma_id=batepapo.usuarioturma.turma.id)  # Redireciona para a URL desejada após a atualização
    else:
        form = Bate_papoForm(instance=batepapo)

    return render(request, "turtem/batepapo/update.html", {'form': form, 'id': mensagem_id})