from django.urls import path

from . import views

urlpatterns = [ 
   path("read/<int:atividade_id>", views.read_comentario, name="read_comentario"),
   path("update/<int:comentario_id>", views.update_comentario, name="update_comentario"),
   path("delete/<int:comentario_id>", views.delete_comentario, name="delete_comentario"),

]