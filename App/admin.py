from django.contrib import admin
from .models import EmployeeRegister

@admin.register(EmployeeRegister)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['idno','name','email','password']
