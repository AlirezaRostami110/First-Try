from django.db import models

# Create your models here.


class Student(models.Model):    
    name = models.CharField(max_length=35)
    subject = models.CharField(max_length= 45)
    un_id = models.BigIntegerField()
    verify_date = models.DateField()