from django.db import models

# Create your models here.

class bookSlot(models.Model):
    name = models.CharField(max_length=100)
    TimeSlot = models.TimeField()
    Date = models.DateField()
    c_Name = models.CharField(max_length=50)
    email = models.EmailField()
    
