from django.contrib import admin
from .models import Log

# Register your models here.

class logDetail(admin.ModelAdmin):
    list_display = ('F_name', 'l_name','email','password','password1')


admin.site.register(Log, logDetail)