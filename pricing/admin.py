from django.contrib import admin
from .models import PlanFeature, PricePlan
# Register your models here.

class PriceFeautreAdmin(admin.ModelAdmin):
    list_display = ('text', 'description',) 
    ordering = ('text',)
    filter_horizontal = ('price_plan',)
    # list_editable = ('price_plan',)


class PricePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','is_special', 'price', )
    list_editable = ('price',)


admin.site.register(PlanFeature,PriceFeautreAdmin)
admin.site.register(PricePlan,PricePlanAdmin)