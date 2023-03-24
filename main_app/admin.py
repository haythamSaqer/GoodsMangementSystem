from django.contrib import admin
from .models import CustomUser, Order, ShippingCompany, Picture


admin.site.register(CustomUser)
admin.site.register(ShippingCompany)
admin.site.register(Order)
admin.site.register(Picture)
