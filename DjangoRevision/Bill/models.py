from django.db import models

# Create your models here.

CHOICE=(( ('ThumsUp','ThumsUp'),('Sprite','Sprite'),('Pepsi','Pepsi'),('Maaja','Maaja'),('Limca','Limca')))
VOLUME=((('200ml','200ml'),('500ml','500ml'),('1000ml','1000ml'),('2500ml','2500ml')))

class Order(models.Model):
    Item=models.CharField(choices=CHOICE,max_length=100)
    Volume=models.CharField(choices=VOLUME,max_length=100)
    Quantity=models.IntegerField()
    