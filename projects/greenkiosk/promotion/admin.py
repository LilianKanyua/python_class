from django.contrib import admin
from .models import Promotion

class PromotionAdmin(admin.ModelAdmin):
    list_display = ("product_name","description","discount","start_date","end_date")


# Register your models here.
admin.site.register (Promotion,PromotionAdmin)
