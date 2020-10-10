from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email =models.EmailField()
    startdate = models.DateField(default=datetime.datetime.now())
    enddate = models.DateField(null=True)
    salary = models.FloatField(default=0.0)
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    def __str__(self): 
        return self.email