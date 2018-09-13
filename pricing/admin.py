from django.contrib import admin
from .models import PlanFeature, PricePlan
# Register your models here.

class PriceFeautreAdmin(admin.ModelAdmin):
    list_display = ('text', 'description', 'price_plan',)
    ordering = ('price_plan',)


class PricePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_special', 'price', )


admin.site.register(PlanFeature,PriceFeautreAdmin)
admin.site.register(PricePlan,PricePlanAdmin)