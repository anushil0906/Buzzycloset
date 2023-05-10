from django.contrib import admin
from .models import Product,Category,Subcategory,Filtersize,Size,Color,HappyCustomer,InstaVideo,ReviewRating


class ColorAdmin(admin.ModelAdmin):
	list_display = ['color_name',]
	list_display_links = ['color_name',]

class HappyCustomerAdmin(admin.ModelAdmin):
	list_display = ['customer_name', 'customer_thought',]
	list_display_links = ['customer_name', 'customer_thought',]

class ReviewRatingAdmin(admin.ModelAdmin):
	list_display = ['product', 'user','review','rating','status',]
	list_display_links = ['product', 'user','review','rating',]
	list_editable = ['status',]
	
class SizeAdmin(admin.ModelAdmin):
	list_display = ['size_num',]
	list_display_links = ['size_num',]	
	
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','actualprice','discount','disigncolor','tshirtcolor','is_featured',]
    list_display_links = ['name',]
    list_editable = ['price','actualprice','discount','disigncolor','tshirtcolor','is_featured',]
    search_fields = ['name','subcategory__name',]
    list_filter = ['subcategory__name',]
	
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product,ProductAdmin)
admin.site.register(Filtersize)
admin.site.register(Size,SizeAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(HappyCustomer,HappyCustomerAdmin)
admin.site.register(InstaVideo)
admin.site.register(ReviewRating,ReviewRatingAdmin)