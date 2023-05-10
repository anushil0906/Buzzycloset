from django.contrib import admin
from .models import Order,OrderPhoto,ShipAuthToken,Coupon

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id_char' , 'user' , 'payment' , 'payment_status' , 'shipment_id',]
    list_display_links = ['order_id_char' , 'user',]
    list_editable = ['payment' , 'payment_status' , 'shipment_id',]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderPhoto)
admin.site.register(ShipAuthToken)
admin.site.register(Coupon)
