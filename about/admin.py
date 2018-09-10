from django.contrib import admin
from django.db import models
from .models import About

from pagedown.widgets import AdminPagedownWidget
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(About, AboutAdmin)
