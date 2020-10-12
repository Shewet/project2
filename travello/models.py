from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    img=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    special_offer=models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"