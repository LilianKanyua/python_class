from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("products","total_price","quantity","payment_method")



# Register your models here.
admin.site.register (Order,OrderAdmin)
