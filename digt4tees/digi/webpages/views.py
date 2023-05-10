from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Product,Category,Subcategory,Filtersize,Size,Color,HappyCustomer,InstaVideo,ReviewRating
from .forms import ReviewForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.template.defaulttags import register
from django.http import JsonResponse
from Cart.cart import Cart
from Cart.models import Order,OrderPhoto
import http.client, urllib.parse
import requests
import json
from django.contrib import messages
import ast
# Create your views here.
from django.template.defaulttags import register
import base64
from django.http import HttpResponse



...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def success(request):
	return render(request,'webpages/success.html')


def vendor(request):
	if request.user.username == 'ytrewq':
		order = Order.objects.order_by('-order_id')
		orderphoto =OrderPhoto.objects.all()
		return render(request,'webpages/vendor.html',{'order':order,'orderphoto':orderphoto})
	return HttpResponse('hehehehehhehehehe')

def vendordetail(request,id):
	
	if request.user.username == 'ytrewq':
		order = get_object_or_404(Order,order_id=id)
		orderphotos = OrderPhoto.objects.filter(order=order)
		d = ast.literal_eval(order.items_json)
		slugs = []
		drive = []
		for i in list(d.keys()):
			product = get_object_or_404(Product,name=i.split(',')[0][1:len(i.split(',')[0])-1])
			slugs.append(product.slug)
			drive.append(product.imagedrive)

			context = zip(orderphotos,list(d.values()),list(d.keys()),slugs,drive)
		return render(request,'webpages/vendordetails.html',{'order':order,'context':context})
	return HttpResponse('hehehehehhehehehe')	


def customize(request):
    
        
    return render(request,'webpages/customize.html') 

	 
def category(request):
	data = {}
	happy_cust = HappyCustomer.objects.all()
	insta_vi = InstaVideo.objects.all()
	response = None
	category = Category.objects.all()
	product = Product.objects.all()
	cart = Cart(request)
	total_bill = 0.0
	for key,value in request.session['cart'].items():
		total_bill = total_bill + (float(value['price']) * value['quantity'])
   
	data['category'] = category
	data['total_bill']  = total_bill
	data['featuredproduct']  = product
	data['HappyCustomers'] = happy_cust
	data['InstaVideos'] = insta_vi
	return render(request,'webpages/home.html',data)



def category_detail(request,id):
	categorys = get_object_or_404(Category,pk=id)
	subcat = Subcategory.objects.filter(category=categorys)
	cart = Cart(request)
	total_bill = 0.0
	for key,value in request.session['cart'].items():
		total_bill = total_bill + (float(value['price']) * value['quantity'])
	request.session['ids'] = id
	data = {
	    'subcat' : subcat,
	    'total_bill':total_bill
	}

	return render(request,'webpages/category.html',data)	


def subcategory_detail(request,slug):
	subcategorys = get_object_or_404(Subcategory,slug=slug)
	product = Product.objects.filter(subcategory=subcategorys)
	cart = Cart(request)
	total_bill = 0.0
	for key,value in request.session['cart'].items():
		total_bill = total_bill + (float(value['price']) * value['quantity'])
	data = {
	    'product' : product,
	    'total_bill': total_bill
	 }
	return render(request,'webpages/layout.html',data)



def product_detail(request,slug):
	data = {}
	featproduct = Product.objects.all()
	product = get_object_or_404(Product,slug=slug)
	
	cart = Cart(request)
	total_bill = 0.0
	for key,value in request.session['cart'].items():
		total_bill = total_bill + (float(value['price']) * value['quantity'])
	size =  Filtersize.objects.filter(name=product.size)
	review = ReviewRating.objects.filter(product_id=product,status=True)
	data['reviews'] = review
	data['product'] =  product
	data['total_bill']  = total_bill
	data['sizes'] =  product.sizes.all()
	data['colors'] = product.colors.all()
	data['featproduct'] = featproduct
	for i in size:
		data['top'] = i.top
		data['left'] = i.left
		data['hight'] = i.hight
		data['width'] = i.width

	
	return render(request,'webpages/product2.html',data)



def success(request):
	return render(request,'webpages/success.html')
    
def search(request):
	categorys = Products.objects.order_by('-created_date')

	

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			categorys = categorys.filter(description__icontains=keyword)
	return render(request,'webpages/search.html',{'categorys':categorys})	

	

def services(request):
	return render(request,'webpages/home.html')

def contact(request):
	return render(request,'webpages/home.html')

def aboutus(request):
	return render(request,'webpages/aboutus.html')

def tc(request):
	return render(request,'webpages/tc.html')	

def pp(request):
	return render(request,'webpages/pp.html')

def rp(request):
	return render(request,'webpages/rp.html')
	
def shipping(request):
	return render(request,'webpages/shipping.html')	

def submit_review(request,id):
	url = request.META.get('HTTP_REFERER')
	if request.method == 'POST':
		try:
			#product = Product.objects.get(slug=slug)
			#print(product)
			reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=id)
			form = ReviewForm(request.POST,instance=reviews)
			form.save()
			messages.success(request,'Thank You! Your review is Updated')
			return redirect(url)
		except ReviewRating.DoesNotExist:
			form = ReviewForm(request.POST)
			if form.is_valid():
				data = ReviewRating()
				
				data.rating = form.cleaned_data['rating']
				data.review = form.cleaned_data['review']
				data.ip = request.META.get('REMOTE_ADDR')
				data.product_id = id
				data.user_id = request.user.id
				data.save()
				messages.success(request,'Thank You for your review!')
				return redirect(url)	