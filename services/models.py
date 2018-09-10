from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=500)
    icon  = models.CharField(max_length=500)
    description = models.TextField()


    def __str__(self):
        return self.title