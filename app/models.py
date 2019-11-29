from django.db import models

# Create your models here.
class Adventure(models.Model):
    duration = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    days = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    price = models.FloatField()

    def __str__(self):
        return self.name