from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from webpages.models import Product,Category,Subcategory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .cart import Cart
import string
from .models import Order,OrderPhoto,ShipAuthToken,Coupon
import base64
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.core.mail import EmailMultiAlternatives
from digi import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from io import BytesIO
from django.template.loader import get_template
import re
import pickle
import razorpay
from django.core.mail import send_mail
from django.contrib import messages 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import datetime
import hmac
import hashlib



from requests.exceptions import HTTPError
#retrieve API key from environment variables


razorpay_id = 'rzp_test_V0W51gkBR8vflQ'
razorpay_account_id = 'Z7e60XDngfrollICRSymAA4w'
razorpay_client = razorpay.Client(auth=(razorpay_id,razorpay_account_id))

add = ""
details= {}
myzip  = []
dicts = {}


def cart_add_featured(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect('home')

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

def cart_add(request, slug):
    x = ''
    y = ''
    z = ''
    if request.method == "POST": 
        y = request.POST['imgBase64']
        if request.POST['colorT']  in ('white','black','blue') :
            x = request.POST['colorT']
        if request.POST['sizeT'] in ('S' ,'L','M','XL','XXL') : 
            z = request.POST['sizeT']
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    print(x)
    print(z)
    cart.add(product=product,image=y,sizeT=z,colorT=x)
    data= {'len':len(request.session['cart'])} 
   
  
           
    return JsonResponse(data)    



def img_add(request):
    cart = Cart(request)
    data= {'len':len(request.session['cart'])}    
    return JsonResponse(data)
    


#@login_required(login_url="/users/login")
def item_clear(request, slug):
    colorT = ''
    sizeT = ''
    if request.GET['colorT']  in ('white','black','blue') :
        colorT = request.GET['colorT']
    if request.GET['sizeT'] in ('S' ,'L','M','XL','XXL') : 
        sizeT = request.GET['sizeT']
    cart = Cart(request)    
    product = Product.objects.get(slug=slug)
    print(colorT)
    print(sizeT)
    cart.remove(product=product,colorT=colorT,sizeT=sizeT)
    total_bill = cart_detail(request)
    data={'d':"done",'total_bill':total_bill}
    return  JsonResponse(data) 


#@login_required(login_url="/users/login")
def item_increment(request, slug):
    if request.GET['colorT'] in ('white','black','blue') :
        colorT = request.GET['colorT']
    if request.GET['sizeT']  in ('S' , 'L','M','XL','XXL') : 
     sizeT = request.GET['sizeT']
    
    Q = 0 
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.add(product=product,image='',colorT=colorT,sizeT=sizeT)
    for value in request.session['cart'].values():
        if value['product_id'] == str(product.id)+sizeT+colorT:
            Q = value['quantity']
            break;
    total_bill = cart_detail(request)        
    data= {'Q':Q,'total_bill':total_bill}    
    return JsonResponse(data)        




    
  

#@login_required(login_url="/users/login")
def item_decrement(request, slug):
    if request.GET['colorT'] in ('white','black','blue') :
        colorT = request.GET['colorT']
    if request.GET['sizeT']  in ('S' , 'L','M','XL','XXL') : 
        sizeT = request.GET['sizeT']
    Q = 0 
    cart = Cart(request)
    product = Product.objects.get(slug=slug)
    cart.decrement(product=product,colorT=colorT,sizeT=sizeT)
    for value in request.session['cart'].values():
        if value['product_id'] == str(product.id)+sizeT+colorT:
            Q = value['quantity']
            break;
    total_bill = cart_detail(request)        
    data = {'Q':Q,'total_bill':total_bill}    
    return JsonResponse(data)   
   

#@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("home")


#@login_required(login_url="/users/login")
def cart_detail(request):
    cart = Cart(request)
    total_bill = 0.0
    for key,value in request.session['cart'].items():
        total_bill = total_bill + (float(value['price']) * value['quantity'])
    return total_bill


  
def codcharge(request):
    total_bill = 0.0
    for key,value in request.session['cart'].items():
        total_bill = total_bill + (float(value['price']) * value['quantity'])
    total_bill= total_bill + 50.0
    data = {'total_bill':total_bill} 
    return JsonResponse(data)
    
    

def placeorder(request,order_db,x):
      token = ""
      for i in ShipAuthToken.objects.all():
          token = i.token
          
      
      url = "https://apiv2.shiprocket.in/v1/external/orders/create/adhoc"
      headers = {"Content-Type": "application/json; charset=utf-8","Authorization": "Bearer"+token}
      order_details = []
      for key,value in request.session['cart'].items():
        order_details.append({
            "name": value['name'],
            "sku": str('('+value['name']+')'+value['colorT']+value['sizeT']),
            "units": value['quantity'],
            "selling_price": value['price'],
            "discount": "",
            "tax": "",
            "hsn": 610910
            })
        data = {
        "order_id": order_db.order_id_char,
        "order_date": datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S"),
        "pickup_location": "Primaryx",
        "channel_id": "3131135",
        "comment": "BUZZY CLOSET",
        "billing_customer_name": order_db.name,
        "billing_last_name":"",
        "billing_address": order_db.address,
        "billing_address_2": "",
        "billing_city": order_db.city,
        "billing_pincode": order_db.zip_code,
        "billing_state": order_db.state,
        "billing_country": "India",
        "billing_email": order_db.email,
        "billing_phone": order_db.phone,
        "shipping_is_billing": True,
        "shipping_customer_name": "",
        "shipping_last_name": "",
        "shipping_address": "",
        "shipping_address_2": "",
        "shipping_city": "",
        "shipping_pincode": "",
        "shipping_country": "",
        "shipping_state": "",
        "shipping_email": "",
        "shipping_phone": "",
        "order_items": order_details,
        "payment_method": x,
        "shipping_charges": 0,
        "giftwrap_charges": 0,
        "transaction_charges": 0,
        "total_discount": 0,
        "sub_total": order_db.total,
        "length": 12,
        "breadth": 9,
        "height": 1,
        "weight": 0.2
        }
        response = requests.post(url, headers=headers, json=data)
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
        data_json = response.json()
        print(data_json.get('shipment_id'))
        order_db.shipment_id = str(data_json.get('shipment_id'))
        order_db.save()       

@login_required(login_url='login')
def checkout(request):
    

  
    global myzip
    
    dicts = {}
    total_bill = 0.0
    total_discount= 0.0
    total_quantity=0
    coupon_error = None
    coupon_success = None
    discount = 0.0
    coupons = None
    
           
   
    item = []
    quant = []
    price = []
    timages = []
    photo = []
    
    for key,value in request.session['cart'].items():
        item.append(value['name'])
        quant.append(value['quantity'])
        price.append(value['price'])
        timages.append(value['image'])
        dicts['('+value['name']+')'+','+value['colorT']+','+value['sizeT']] = value['quantity']
        total_bill = total_bill + (float(value['price']) * value['quantity'])
        total_discount = total_discount + (float(value['discount']) * value['quantity'])
        total_quantity= total_quantity + value['quantity']
        
    
    myzip = zip(item,quant,price)
    final_bill = total_bill
    
    
        
    if request.method == 'GET':
        data= {}
        coupon = request.GET.get('coupon','')
        pay = request.GET.get('pay','')
        if coupon:
            try:
                coupon_code = Coupon.objects.filter(active=True)
                for i in coupon_code:
                    if i.coupon == coupon:
                        coupons = i.coupon
                        discount = i.discount
                        coupon_success = "Hurray! Coupon Code applied and you Saved ₹{}".format(discount)
                        if pay == 'prepaid':
                            total_bill = total_bill - discount
                        else :
                            total_bill = total_bill - discount+10.0
                        data['total_bill'] = total_bill
                        
                        return JsonResponse(data)
                    else :
                        if pay == 'cod':
                            total_bill = total_bill + 10.0
                        data['total_bill'] = total_bill
                        return JsonResponse(data)
                        
        
            
            except:
                coupon_error = 'invalid coupon code'
        elif pay == 'cod'  and coupon == '' :
            total_bill = total_bill + 10.0
            data['total_bill'] = total_bill
            return JsonResponse(data)        
        elif pay == 'prepaid'  and coupon == '' :
            data['total_bill'] = total_bill
            return JsonResponse(data)    
            
                
    
    if  request.method=="GET" and len(request.session['cart'])== 0:
        return render(request,'cart/emptycart.html')
    if request.method=="POST":
        coupon = request.POST['coupon']
        name = request.POST['firstname']+request.POST['lastname']
        address = request.POST['address_1']+request.POST['address_2']
        city = request.POST['city']
        email = request.POST['email']
        user = request.user.username
        state = request.POST['state']
        phone = request.POST['telephone']
        zip_code = request.POST['postcode']
        payment = request.POST['payment-method']
        string_check= re.compile('[\'=!"%^\&*()<>?|}{~:]')
        if string_check.search(name)==None and string_check.search(address)==None and string_check.search(city)==None and string_check.search(email)==None and string_check.search(state)==None and string_check.search(phone)==None and string_check.search(zip_code)==None and string_check.search(payment)==None :
            if coupon:
                coupon_code = Coupon.objects.filter(active=True)
                for i in coupon_code:
                    if i.coupon == coupon:
                        coupons = i.coupon
                        discount = i.discount
                        total_bill = total_bill - discount
        
          
            order_db = Order(items_json = dicts,name = name,total = total_bill,address = address,city = city,state = state,email = email,user = user,phone = phone,zip_code = zip_code,payment=payment)
            
            
            if payment == 'prepaid':
                 
                order_amount = int(total_bill)*100
                order_currency = 'INR'
                callback_url = 'http://127.0.0.1:8000/Cart/handlerequest/'
                print(callback_url)
                notes = {'order-type': "basic order from the website", 'key':'value'}
                razorpay_order = razorpay_client.order.create(dict(amount=order_amount, currency=order_currency, notes = notes, receipt=order_db.order_id, payment_capture='0'))
                print(razorpay_order['id'])
                order_db.razorpay_order_id = razorpay_order['id']
                orderssss = Order.objects.filter(user=request.user.username,payment_status=3)
                if orderssss != None:
                    orderssss.delete()
                order_db.save()
                for image in timages:
                    photo = OrderPhoto.objects.create(order= order_db,photo=image)
                return render(request, 'cart/paymentsummaryrazorpay.html', {'order':order_db, 'order_id': razorpay_order['id'], 'orderId':order_db.order_id, 'final_price':total_bill, 'razorpay_merchant_id':razorpay_id, 'callback_url':callback_url})
            elif payment == 'cod':
                total_bill = total_bill+10.0
                
                
            
                
                if len(request.session['cart'])== 0:
                    return render(request,'cart/emptycart.html')
                
                
                            
                else:
                    orderx = Order.objects.filter(user=request.user.username,payment_status=3)
                    if orderx != None:
                        orderx.delete()
                    
                    order = Order(items_json = dicts,name = name,total = total_bill,address = address,city = city,state = state,email = email,user = user,phone = phone,zip_code = zip_code,payment=payment,payment_status = 4)
                    order.save()
                    for image in timages:
                        photo = OrderPhoto.objects.create(order=order,photo=image)
                    placeorder(request,order,'cod')
                    cart = Cart(request)
                    cart.clear()
                    return redirect('success')
            else :
                return HttpResponse('no such payment choice exist')
        else :
            messages.warning(request,"special characters are not allowed")
                

        
        

    return render(request,'cart/checkout.html',{'dicts':dicts,'total_discount':total_discount,'total_bill':total_bill,'coupons':coupons,'coupon_error':coupon_error,'discount':discount,'coupon_success':coupon_success,})    





def hmac_sha256(data_str,secret):
    return hmac.new(secret.encode(), data_str.encode(), hashlib.sha256).hexdigest()


        


@csrf_exempt
def handlerequest(request):

    if request.method == "POST":
        try :
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            try :
                order_db = Order.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505sssss Not Found")
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            
            generated_signature = hmac_sha256(order_id + "|" + payment_id,razorpay_account_id)
            if generated_signature == signature :
                amount = order_db.total*100  
                try :
                    razorpay_client.payment.capture(payment_id, amount)
                    order_db.payment_status = 1
                    order_db.save()
                    order_db = Order.objects.get(order_id=order_db.order_id)
                    placeorder(request,order_db,'prepaid')
  
  
               
                   
                   
                     



                    ## For generating Invoice PDF
                    '''
                    template = get_template('cart/invoice.html')
                    data = {
                        'order_id': str(order_db.order_id),
                        'transaction_id': order_db.razorpay_payment_id,
                        'user_email': order_db.email,
                        'name': order_db.user,
                        'order': order_db,
                        'mylist':myzip,
                        'amount':str( order_db.total),
                    }
                    html  = template.render(data)
                    result = BytesIO()
                    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
                    pdf = result.getvalue()
                    filename = 'Invoice_' + data['order_id'] + '.pdf'

                    mail_subject = 'Recent Order Details'
                    message = render_to_string('cart/emailinvoice.html', {
                         'user': order_db.user,
                         'order': order_db,
                         'mylist':myzip,
                     })
                    context_dict = {
                        'user': order_db.user,
                        'order': order_db
                    }
                    template = get_template('cart/emailinvoice.html')
                    message  = template.render(context_dict)
                    to_email = order_db.email
                    #email = EmailMessage(
                     #    mail_subject,
                      #   message, 
                       #  settings.EMAIL_HOST_USER,
                       #  [to_email]
                     #)

                    # for including css(only inline css works) in mail and remove autoescape off
                    email = EmailMultiAlternatives(
                        mail_subject,
                        "hello",       # necessary to pass some message here
                        settings.EMAIL_HOST_USER,
                        [to_email,]
                    )
                    email.attach_alternative(message, "text/html")
                    email.attach(filename, pdf, 'application/pdf')
                    email.send(fail_silently=True)
                    '''
                    
                
                    cart = Cart(request)
                    cart.clear()
                    return redirect ('success')
                except:
                    order_db.payment_status = 2
                    order_db.save()
                    return render(request, 'cart/paymentfailed.html')
            else:
                order_db.payment_status = 2
                order_db.save()
                return render(request, 'cart/paymentfailed.html')
        except:
            return HttpResponse("505 not found")        
       
