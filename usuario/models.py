from django.contrib.auth.models import User
from django.db import models



class Usuario(User):



    def __str__(self):
        return self.username

    