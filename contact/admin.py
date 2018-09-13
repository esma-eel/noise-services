from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('name', 'email', 'phone','which_price_plan' ,'message', 'file')


admin.site.register(Contact,ContactAdmin)

admin.site.register(ContactIntro)