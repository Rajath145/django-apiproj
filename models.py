from django.db import models

# Create your models here.

class Trains(models.Model):
    name=models.CharField(max_length=100)
    train_no=models.IntegerField()
    starting=models.CharField(max_length=100)
    ending=models.CharField(max_length=100)
    price=models.IntegerField()
    timings=models.TimeField()
    type=models.CharField(max_length=100)



