from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("customer_name","amount","payment_method_name","payment_method","payment_description")



# Register your models here.
admin.site.register (Payment,PaymentAdmin)

# Register your models here.
