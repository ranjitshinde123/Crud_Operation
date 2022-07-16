from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Record)
class recordadmin(admin.ModelAdmin):
    list_display = ['id','ename','email','mobile','password']