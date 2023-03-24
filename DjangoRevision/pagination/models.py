from django.db import models

# Create your models here.

class People(models.Model):
    Name=models.CharField(max_length=20)
    Location=models.CharField(max_length=20)
    passby=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.Name