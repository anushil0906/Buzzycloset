from django.db import models
from django.contrib.auth.models import User
import string
import random
import requests
from PIL import Image
 
from django.http import HttpResponse
from django.http import HttpResponse




from datetime import datetime,timedelta
# Create your models here.

CHOICES = (
    ("Order Recieved", "Order Recieved"),
    ("Out for delivery", "Out for delivery"),
    ("Mid Way", "Mid Way"),
    ("Delivered", "Delivered"),
    
    )



# Create your models here.








def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))



class Order (models.Model):
	payment_choices=(
		  ('prepaid','prepaid'),
		  ('cod','cod'),
		  

		)
   
	payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
        (4,'PENDING CASH'),
        (5,'Order cancelled and refund processed')
    )


	order_id = models.AutoField(primary_key=True)
	order_id_char = models.CharField(max_length=255,default='')
	items_json = models.CharField(max_length=5000)
	total = models.IntegerField(null=True, default=100)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	user = models.CharField(max_length=200,default="")
	state = models.CharField(max_length=255)
	zip_code = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	status = models.CharField(max_length=100 , choices = CHOICES , default="Order Recieved")
	payment = models.CharField(choices=payment_choices,max_length=255,default="")
	shipment_id = models.CharField(max_length=15,default="")
	payment_status = models.IntegerField(choices = payment_status_choices, default=3)
	razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
	razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
	razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		if not len(self.order_id_char):
			self.order_id_char = random_string_generator()
		return super(Order, self).save(*args, **kwargs)	


	
class OrderPhoto(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='photos')
	photo = models.TextField()
	

class ShipAuthToken(models.Model):
    token = models.CharField(max_length=1000)
    
    
class Coupon(models.Model):
    coupon = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

	# resizing the image, you can change parameters like size and quality.
	
	







	

	
	


