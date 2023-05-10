from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from webpages.models import Product
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import re
from django.contrib import auth
from django.contrib import messages 
from Cart.models import Order,OrderPhoto,ShipAuthToken
import json
import requests
from math import ceil
import ast
import datetime
# Create your views here.
from django.http import HttpResponse


# Create your views here.



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		string_check= re.compile('[\'=!"%^&*()<>?/\|}{~:]')
		password_check= re.compile('\'"/')

		user = auth.authenticate(username=username,password=password)

		if user is not None and  string_check.search(username) == None and password_check.search(password) == None:
			auth.login(request,user)
			messages.success(request,'you are logged in')
			return redirect('home')
		elif user is  None and  string_check.search(username) != None or password_check.search(password) != None:
		    messages.warning(request,'invalid credentials')
		    return redirect('login')
		else:
		    messages.warning(request,'invalid credentials')
		    return redirect('login')	
	return render(request,'accounts/login.html')


def register(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		
		email = request.POST['email']
		password = request.POST['password']
		
		string_check= re.compile('[\'=!"%^&*()<>?/\|}{~:]')
		password_check= re.compile('\'"/')


		if (string_check.search(email) == None) and (password_check.search(password) == None) and (string_check.search(username) == None) :


			
			if User.objects.filter(email=email).exists():
				messages.warning(request,'email exists')
				return redirect('register')
			
			if User.objects.filter(username=username).exists():
				messages.warning(request,'Username exists')
				return redirect('register')
			
			else:
				user = User.objects.create_user(username=username,email=email,password=password)
				user.save()
				messages.success(request,"Account is register successfully")
				return redirect('login')
			    

		elif (string_check.search(email) != None)  or (password_check.search(password) != None) or (string_check.search(username) != None):

		    messages.warning(request,"special characters are not allowed")
		else :
			messages.warning(request,"password not match")
		    	

		
	return render(request,'accounts/register.html')

def logouts(request):
	logout(request)
	return redirect('home')


"""
def cancel(request):
    message = ""
    last = 0
    order = Order.objects.all()
    user = request.user
    
    for i in order:
        if user.username == i.user:
            last = i.order_id
    orderx = Order.objects.filter(order_id=last).first()        
    if request.method == "POST":
        response = request.POST['response']
        if response == 'yes':
            
            if orderx.status=="Delivered" or orderx.status=="Out for delivery":
                message = "sorry you can't cancel the order as it is out for delivery!!!!"
                return render(request,'accounts/Cancel.html',{'message':message})
            else:
                
                orderx.payment_status = 5
                orderx.save()
                message = "Order cancelled and refund processed"
                return render(request,'accounts/Cancel.html',{'message':message})
                
                

        
        
    return render(request,'accounts/Cancel.html')
"""
def track(shipmentid):
    token = ""
    for i in ShipAuthToken.objects.all():
        token = i.token

    print(token) 
    print(shipmentid)   
    
    url = "https://apiv2.shiprocket.in/v1/external/courier/track/shipment/"+shipmentid
    headers = {"Content-Type": "application/json; charset=utf-8","Authorization": "Bearer"+token}
    response = requests.get(url, headers=headers)
    return response.json()
	
def tracker(request):
	order = Order.objects.all()
	return render(request,'accounts/profile.html')
def latestorder(request):
	last = 0
	status  = ''
	last_order = ""
	time = ""
	last_order_id  = ""
	order = Order.objects.all()
	for i in order:
		if request.user.username == i.user:
			last = i.order_id
			last_order = i.items_json
			last_order_id = i.order_id_char
			time = i.timestamp
			status  = i.payment
		
	return render(request,'accounts/profile.html',{'order':order,'status':status,'last_order':last_order,'last':last,'time':time,'last_order_id':last_order_id})		


def allorders(request):
    count = 0
    order = Order.objects.all()
    current_datetime = datetime.datetime.now()
    return render(request,'accounts/allorders.html',{'order':order,'current_datetime':current_datetime})

def orderdetail(request,id):
	order = get_object_or_404(Order,order_id=id)
	
	if request.user.username == order.user:
		orderphotos = OrderPhoto.objects.filter(order=order)
		d = ast.literal_eval(order.items_json)
		context = []
		prices = []
		products = []
		for i in list(d.keys()):
			product = get_object_or_404(Product,name=i.split(',')[0][1:len(i.split(',')[0])-1])
			prices.append(product.price)
			products.append(product)
			context = zip(orderphotos,list(d.values()),list(d.keys()),prices,products)
		#print(order)
		#trackorder 	= track(order.shipment_id)
		#print(trackorder)
		"""

		if trackorder['tracking_data']['track_status'] != 0:
		    track_url = trackorder['tracking_data']['track_url']
		    ts = trackorder['tracking_data']['shipment_track']
		    track_status = ts[0]['current_status']
		else:    
		    track_url = 'Will be updated soon'
		    track_status = 'Order Recieved'"""
		return render(request,'accounts/orderdetail.html',{'order':order,'context':context})    
		#return render(request,'accounts/orderdetail.html',{'order':order,'context':context,'trackorder': trackorder,'track_url':track_url,'track_status':track_status })
	return render(request,'accounts/orderdetail.html')