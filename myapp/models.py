from django.db import models


# Create your models here.

class CakeBox(models.Model):
    name=models.CharField(max_length=250)
    flavour=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=250)
    weight=models.CharField(max_length=100)
    layer=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",null=True,blank=True)

    def __str__(self):
        return self.name

