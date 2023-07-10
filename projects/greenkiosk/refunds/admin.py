from django.contrib import admin
from .models import Refunds


class RefundsAdmin(admin.ModelAdmin):
    refund_list= ("Order_number","amount","reason","created_date")


# Register your models here.

admin.site.register(Refunds,RefundsAdmin)