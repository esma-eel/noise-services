from django.contrib import admin
from .models import Customers, CustomersIntro
# Register your models here.
class CustomerIntroAdmin(admin.ModelAdmin):
    list_display = ('title', 'description' ,'active',)
    list_editable = ('active',)


admin.site.register(Customers)
admin.site.register(CustomersIntro,CustomerIntroAdmin)