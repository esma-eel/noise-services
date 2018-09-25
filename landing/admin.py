from django.contrib import admin
from .models import Navigation
# Register your models here.

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_field', 'full_url', 'for_footer',)


admin.site.register(Navigation,NavigationAdmin)