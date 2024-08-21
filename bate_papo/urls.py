from django.urls import path

from . import views

urlpatterns = [ 
    path("read/<int:turma_id>", views.read_batepapo, name="read_batepapo"),
    path("update/<int:mensagem_id>", views.update_batepapo, name="update_batepapo"),


]