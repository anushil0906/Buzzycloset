from django.urls import path
from . import views

urlpatterns = [
    #path('codcharge/', views.codcharge, name='cod'),
    path('add/<slug:slug>/', views.cart_add, name='cart_add'),
    #path('imageadd/<slug:slug>/',views.img_add, name='img_add'),
   

    path('item_clear/<slug:slug>/', views.item_clear, name='item_clear'),
    path('item_increment/<slug:slug>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<slug:slug>/',
         views.item_decrement, name='item_decrement'),  
    
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/',views.checkout,name='checkout'),

    path('handlerequest/',views.handlerequest,name="HandleRequest"),
    

]