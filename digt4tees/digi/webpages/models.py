from django.db import models
from datetime import datetime
import string
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='media/tees/%y/%m/',default="")
	def __str__(self):
		return self.name 

class Subcategory(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='media/tees/%y/%m/',default="")
	category = models.ForeignKey(Category,  on_delete = models.CASCADE)
	def __str__(self):
		return self.name

class Size(models.Model):
    size_num = models.CharField(max_length=10)
    

class Color(models.Model):
    color_name = models.CharField(max_length=15)
    
class Product(models.Model):

	disign_color = (('black','black'),('white','white'))
	tshirt_color = (('black','black'),('white','white'))
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, null=True, blank=True)
	actualprice = models.IntegerField(null=True, blank=True)
	discount = models.IntegerField(null=True, blank=True)
	price = models.IntegerField()
	image = models.ImageField(upload_to='media/tees/%y/%m/')
	imagedrive = models.CharField(max_length=255, null=True)
	description = RichTextField(blank=True)
	size_choices=(('large','large'),('medium','medium'),('logo','logo'),('small','small'),('mediumless','mediumless'),('hightless',
	'hightless'),('topcenter','topcenter'),('bottom','bottom'),('bottomleft','bottomleft'),('bottomright','bottomright'))
	size = models.CharField(choices=size_choices,max_length=255,default="large")
	disigncolor = models.CharField(choices=disign_color,max_length=255,default="white")
	tshirtcolor = models.CharField(choices=tshirt_color,max_length=255,default="white")
	is_featured = models.BooleanField(default=False)
	subcategory = models.ForeignKey(Subcategory,on_delete= models.CASCADE)
	
	sizes = models.ManyToManyField(Size, related_name="product_sizes", null=True, blank=True)
	colors = models.ManyToManyField(Color, related_name="product_colors", null=True, blank=True)
    




	#size = models.ForeignKey(Filtersize,on_delete= models.CASCADE)

	def __str__(self):
		return self.name




class Filtersize(models.Model):
	size_choices=(('large','large'),('medium','medium'),('logo','logo'),('small','small'),('mediumless','mediumless'),('hightless',
	'hightless'),('topcenter','topcenter'),('bottom','bottom'),('bottomleft','bottomleft'),('bottomright','bottomright'))
	name = models.CharField(choices=size_choices,max_length=255,default="")
	top = models.CharField(max_length=10)
	left = models.CharField(max_length=10)
	hight = models.IntegerField()
	width = models.IntegerField()
	def __str__(self):
		return self.name



class HappyCustomer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_thought = models.CharField(max_length=1000)
    
    
class InstaVideo(models.Model):
    insta_video = models.FileField(upload_to='instavideos_uploaded',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','mp3'])])


class ReviewRating(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	review = models.TextField(max_length=50,blank=True)
	rating = models.FloatField()
	ip = models.CharField(max_length=20,blank=True)
	status = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.review
