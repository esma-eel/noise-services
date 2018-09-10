from django.db import models

# Create your models here.
class Navigation(models.Model):
    name = models.CharField(max_length=500)
    url_field = models.CharField(max_length=500, null=True, blank=True)
    full_url = models.CharField(max_length=500, null=True, blank=True)

    for_footer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

