from django.urls import path
from . import views

urlpatterns = [
     path('',views.category,name="home"),
     path('<int:id>',views.category_detail,name="detail"),
     path('customize',views.customize,name="customize"),
     path('subcategory/<slug:slug>',views.subcategory_detail,name="subdetail"),
     path('product/<slug:slug>',views.product_detail,name="prodetail"),
     path('vendor',views.vendor,name="vendor"),
     path('success',views.success,name="success"),
     path('vendordetail/<int:id>',views.vendordetail,name="vendordetail"),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('tc/',views.tc,name='tc'),
     path('shipping/',views.shipping,name='shipping'),
     path('pp/',views.pp,name='pp'),
     path('rp/',views.rp,name='rp'),
     path('submit_review/<int:id>',views.submit_review,name='submit_review'),
     
 
     
]