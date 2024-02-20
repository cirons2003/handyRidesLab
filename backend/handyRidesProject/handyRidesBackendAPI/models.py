from django.db import models
from datetime import date

class Person(models.Model):
    name = models.CharField(null = True, max_length = 100)
    city = models.CharField(null = True, max_length = 30)
    state = models.CharField(null = True, max_length = 30) 
    o_city = models.CharField(null = True, max_length = 30)
    o_state = models.CharField(null = True, max_length = 30)
    is_driver = models.BooleanField(default = False)
    max_passengers = models.IntegerField(blank = True, null = True) 
    price = models.IntegerField(blank = True, null = True) 
    description = models.CharField(max_length = 500, blank = True, null = True) 



    
