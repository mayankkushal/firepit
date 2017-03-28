from django.db import models
from django.conf import settings
import cloudinary
import os
from datetime import date
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Banner(models.Model):
	name = models.CharField(default="slideshow", max_length=30)

	def __str__(self):
		return self.name


class SlideShowImage(models.Model):
	slideshow = models.ForeignKey(Banner)
	image = models.ImageField(upload_to='slideshow')
	url = models.URLField(blank=True)
	desc = models.CharField(max_length=300, blank=True)

	def __str__(self):
		return self.image.name

class ReviewControl(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	allowed = models.BooleanField(default=True)

	def __str__(self):
		return self.user.email

	def create_review_control(sender, instance, created, **kwargs):
		if created:
			ReviewControl.objects.create(user=instance)

	post_save.connect(create_review_control, sender=User)


class RequestQuote(models.Model):
	name = models.CharField(max_length=156)
	email = models.EmailField(max_length=256)
	phone_number = models.CharField(max_length=12)
	message = models.TextField(max_length=1256, null=True, blank=True)

	def __str__(self):
		return self.name

def get_quote_image_name(instance, filename):
	name = instance.quote.name

	today = date.today()
	today_path = today.strftime("%Y/%m/%d")
	return "request_quote/%s/%s/%s"%(name,today_path,filename)


class RequestQuoteImage(models.Model):
	quote = models.ForeignKey(RequestQuote, related_name="image")
	image = models.ImageField(upload_to=get_quote_image_name, verbose_name='Image', blank=True, null=True )

	def __str__(self):
		return self.quote.name

	def save(self, *args, **kwargs):
		today = date.today()
		today_path = today.strftime("%Y/%m/%d")
		upload_add = "request_quote/"+self.quote.name+"/"+today_path
		cloudinary.uploader.upload( self.image, folder=upload_add, public_id=os.path.splitext(self.image.name)[0])
		super(RequestQuoteImage, self).save(*args, **kwargs)


def get_space_image_name(instance, filename):
	name = instance.space.name
	today = date.today()
	today_path = today.strftime("%Y/%m/%d")
	return "decorate_space/%s/%s/%s"%(name,today_path,filename)


class DecorateSpace(models.Model):
	name = models.CharField(max_length=156)
	email = models.EmailField(max_length=256)
	phone_number = models.CharField(max_length=12)
	address = models.CharField(max_length=500)
	message = models.TextField(max_length=1256, null=True, blank=True)

	def __str__(self):
		return self.name

class DecorateSpaceImage(models.Model):
	space = models.ForeignKey(DecorateSpace, related_name="image")
	image = models.ImageField(upload_to=get_space_image_name, verbose_name='Image', blank=True, null=True )

	def __str__(self):
		return self.space.name

	def save(self, *args, **kwargs):
		today = date.today()
		today_path = today.strftime("%Y/%m/%d")
		upload_add = "decorate_space/"+self.space.name+"/"+today_path
		cloudinary.uploader.upload( self.image, folder=upload_add, public_id=os.path.splitext(self.image.name)[0])
		super(DecorateSpaceImage, self).save(*args, **kwargs)

class PowerSolutions(models.Model):
	name = models.CharField(max_length=156)
	email = models.EmailField(max_length=256)
	phone_number = models.CharField(max_length=12)
	address = models.CharField(max_length=500)
	message = models.TextField(max_length=1256, null=True, blank=True)
	SMALL_CHOICES = (('0','0'), ('1-3','1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('>10', '>10'))
	small_light = models.CharField(null=True, default='0', max_length=5, choices=SMALL_CHOICES)
	big_light = models.CharField(null=True, default='0', max_length=5, choices=SMALL_CHOICES)
	fan = models.CharField(null=True, default='0', max_length=5, choices=SMALL_CHOICES)
	BIG_CHOICES = (('0','0'), ('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('>5','>5'))
	desktop = models.CharField(null=True, default='0', max_length=5, choices=BIG_CHOICES)
	HOURS_CHOICES = (('3', '3'), ('6','6'), ('9','9'), ('12','12'))
	hours = models.CharField(default='0', max_length=5, choices=HOURS_CHOICES)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Power Solutions"

	def power_total(self):
		total = 0 
		total += self.small_light * 15
		total += self.big_light * 50
		total += self.fan * 100
		total += self.desktop * 100
		return total

	def invertor_category(self, total):
		# this will return the category of invertor to use
		if total <= 560:
			return 1 # 700vs invertor
		elif total > 560 and total <= 720:
			return 2
		elif total > 720 and total < 900:
			return 3
		else:
			return 4
	