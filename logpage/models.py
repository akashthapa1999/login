from django.db import models
# Create your models here.

class User_log(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    pass1 = models.CharField( max_length=50)

