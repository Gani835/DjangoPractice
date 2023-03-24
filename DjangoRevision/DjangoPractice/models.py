from django.db import models

# Create your models here.

class ProductsDetailes(models.Model):
    Product_ID=models.IntegerField()
    Product_Category=models.CharField(max_length=100)
    Product_Name=models.CharField(max_length=100)
    Product_Price=models.IntegerField()
    

class FamilyDetailes(models.Model):
    Father_Name=models.CharField(max_length=20)
    Mother_Name=models.CharField(max_length=20)
    Son_Name=models.CharField(max_length=20)
    