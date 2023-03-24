from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=10)
    Address=models.CharField(max_length=20)
    
class EmployeeList(models.Model):
    Employee_Name=models.CharField(max_length=20)
    Employee_Age=models.IntegerField()
    Employee_Address=models.CharField(max_length=20)
    Employee_Salary=models.IntegerField()
    

    