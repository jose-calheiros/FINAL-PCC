from django.urls import path

from . import views

urlpatterns = [
   path("add/<int:experimento_id>", views.add_atividade, name="read_atividade"),
   path("read/<int:experimento_id>", views.read_atividade, name="read_atividade"),
   path("detail/<int:atividade_id>", views.detail_atividade, name="detail_atividade"),
   path("delete/<int:atividade_id>", views.delete, name="delete"),
   path("confdelete/<int:atividade_id>", views.confdelete, name="confdelete"),
   path("update/<int:atividade_id>", views.update, name="update"),




 
]