from django.contrib import admin
from logpage.models import User_log

# Register your models here.

class user(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','pass1',]

admin.site.register(User_log,user)


