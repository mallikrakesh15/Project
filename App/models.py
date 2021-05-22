from django.db import models

class EmployeeRegister(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=30)
