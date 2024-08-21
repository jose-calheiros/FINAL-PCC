from django.urls import path
from . import views

urlpatterns = [
     path("register/", views.register, name="register"),
     path("update/<int:user_id>", views.update, name="update"),
     path("perfil/", views.perfil, name="perfil"),

]

