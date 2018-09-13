from django.db import models

# Create your models here.
from pricing.models import PricePlan
choices_plan = [('هیچکدام','هیچکدام'),]
for price in PricePlan.objects.all():
    choices_plan.append((price.name, price.name))


class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    which_price_plan = models.CharField(max_length=500, choices=choices_plan,default='هیچکدام')
    message = models.TextField()
    file = models.FileField(upload_to='contacts/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)

class ContactIntro(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title