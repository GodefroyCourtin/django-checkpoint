from django.db import models

# Create your models here.
class Voyage(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    linkphoto = models.URLField()

    def __str__(self):
        return self.title


class Step(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    date = models.DateField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.city


class Linkstep(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    linkrestaurant = models.URLField()
    title_step = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title_step
