from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect



class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
            
        self.cart = cart
   




    def add(self, product,image,sizeT,colorT,quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = str(product.id)+sizeT+colorT
        newItem = True
        if str(str(product.id)+sizeT+colorT) not in self.cart.keys():

            self.cart[str(product.id)+sizeT+colorT] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.name,
                'quantity': 1,
                'price': str(product.price),
                'slug': product.slug,
                'image': image,
                'sizeT':sizeT,
                'colorT':colorT,
                'photo':product.image.url,
                'actualprice':product.actualprice,
                'discount':int(product.discount),

            }
            
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(str(product.id)+sizeT+colorT) :

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[str(product.id)+sizeT+colorT] = {
                    'userid': self.request,
                    'product_id': str(product.id)+sizeT+colorT,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'slug': product.slug,
                    'image': image,
                    'sizeT':sizeT,
                    'colorT':colorT,
                    'photo':product.image.url,
                    'actualprice':product.actualprice,
                    'discount':int(product.discount),
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product,sizeT,colorT):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)+sizeT+colorT
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self,product,sizeT,colorT):
        for key, value in self.cart.items():
            if key == str(product.id)+sizeT+colorT:

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True


