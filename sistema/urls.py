from django.urls import path
from . import views


urlpatterns = [
  
   path("read/<int:turma_id>", views.read, name="read"),
   path("add/<int:usuarioturma_id>", views.add, name="add"),
   path("delete/<int:experimento_id>", views.delete, name="delete"),
   path("update/<int:experimento_id>", views.update, name="update"),
   path("confdelete/<int:experimento_id>", views.confdelete, name="confdelete"),
   path("detail/<int:experimento_id>", views.detail, name="detail"),
]