from django.contrib import admin

# Register your models here.
from.models import TaxiDetails,Customer,PaymentReceipt
admin.site.register(TaxiDetails)
admin.site.register(Customer)
admin.site.register(PaymentReceipt)
