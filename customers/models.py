from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='customers/', blank=True, null=True)


    def __str__(self):
        return self.name


class CustomersIntro(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title