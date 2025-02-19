from django.contrib import admin
from .models import My_Model
# Register your models here.
@admin.register(My_Model)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']