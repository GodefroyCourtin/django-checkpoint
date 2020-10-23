from django.db import models

# Create your models here.
class Voyage(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #start_date 
    #end_date
    def __str__(self):
        return self.title

class Voyagestep(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE) 
    city = models.CharField(max_length=200)
    #date
    resume = models.CharField(max_length=800)

    def __str__(self):
        return self.name

class Linkstep(models.Model):
    voyagestep = models.ForeignKey(Voyagestep, on_delete=models.CASCADE) 
    linkrestaurant = models.URLField()
    linkphoto = models.URLField()
    
    
