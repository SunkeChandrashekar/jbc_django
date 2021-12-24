from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    mobileno = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    village = models.TextField()
    password = models.CharField(max_length=20)
    offer = models.BooleanField(default=False)