from django.db import models

# Create your models here.

class Employee(models.Model):
    EmployeeID=models.CharField(max_length=20)
    EmployeeName=models.CharField(max_length=20)
    EmployeeAge=models.IntegerField()
    EmployeeSalary=models.IntegerField(null=True)
    EmployeeDeptNo=models.IntegerField(null=True)
    EmployeeDeptName=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.EmployeeName
    
# OneToOne Reltionship. . . . (Refer database to see what happend with this)

class Customer(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    name=models.CharField(max_length=20)
    Customer=models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )
    
    def __str__(self):
        return self.name
    
# One to many Relationship. . . .

class Customer2(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Vehicle2(models.Model):
    name=models.CharField(max_length=20)
    Customer=models.ForeignKey(
        Customer2,
        on_delete=models.CASCADE,
        related_name='Vehicle2'
    )
    def __str__(self):
        return self.name
    
# Many to many Relationship. . . . . 

class Customer3(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Vehicle3(models.Model):
    name=models.CharField(max_length=20)
    Customer=models.ManyToManyField(
        Customer3,
        related_name='Vehicle3'
    )
    def __str__(self):
        return self.name
    
# Class Based Views. . . . .

class StudentDetailes(models.Model):
    Student_No=models.IntegerField()
    Student_Name=models.CharField(max_length=20)
    Father_Name=models.CharField(max_length=20)
    Student_Age=models.IntegerField()
    Address=models.CharField(max_length=20)
