from django.urls import path
from . import views

urlpatterns = [
    path("", views.read, name='read'),
    path("add", views.add_turma, name='add_turma'),
    path("delete/<int:turma_id>", views.delete, name="delete"),
    path("update/<int:turma_id>", views.update, name="update"),
    path("confdelete/<int:turma_id>", views.confdelete, name="confdelete"),
    path("detail/<int:turma_id>", views.detail, name='detalhes_turma'),
    path("entrar", views.entrar_turma, name='entar_turma')

]