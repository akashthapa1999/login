from django.db import models

# Create your models here.

class Log(models.Model):
    F_name = models.CharField("fname", max_length=50)
    l_name = models.CharField("lname", max_length=50)
    email = models.EmailField("email", max_length=254)
    password =  models.CharField("pass1", max_length=254)
    password1 =  models.CharField("pass2", max_length=254)

