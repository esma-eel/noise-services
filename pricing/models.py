from django.db import models

# Create your models here.
class PlanFeature(models.Model):
    text = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    price_plan = models.ForeignKey('PricePlan', on_delete=models.CASCADE, related_name='plan_features')
    def __str__(self):
        return self.text


class PricePlan(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    # plan_features = models.ManyToManyField('PlanFeature')
    is_special = models.BooleanField(default=False)
    price = models.CharField(max_length=1500)


    def __str__(self):
        return self.name