from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
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