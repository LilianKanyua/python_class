from django.contrib import admin
from .models import Customer

# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    customer= ("first_name","last_name","email","phone","address")


# Register your models here.

admin.site.register(Customer,CustomerAdmin)