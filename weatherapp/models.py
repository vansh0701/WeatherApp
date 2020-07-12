from django.db import models

class WeatherData(models.Model):

      main= models.CharField(max_length=100)
      description=models.CharField(max_length=100)
      icon= models.CharField(max_length=100) 
      base=models.CharField(max_length=100) 
      temp=models.FloatField() 
      feels_like=models.FloatField()  
      temp_min= models.FloatField() 
      temp_max= models.FloatField() 
      pressure=models.IntegerField() 
      humidity= models.IntegerField()