from django.db import models
from django.conf import settings
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
	message = models.TextField(max_length=1256)

	def __str__(self):
		return self.name

def get_quote_image_name(instance, filename):
	name = instance.quote.name
	from datetime import date
	today = date.today()
	today_path = today.strftime("%Y/%m/%d")
	return "request_quote/%s/%s-%s"%(name,today_path,filename)


class RequestQuoteImage(models.Model):
	quote = models.ForeignKey(RequestQuote, related_name="image")
	image = models.ImageField(upload_to=get_quote_image_name, verbose_name='Image', blank=True, null=True )

	def __str__(self):
		return self.quote.name

	def save(self, *args, **kwargs):
		cloudinary.uploader.upload( self.image, folder=get_quote_image_name, public_id=os.path.splitext(self.image.name)[0])

		super(RequestQuoteImage, self).save(*args, **kwargs)


def get_space_image_name(instance, filename):
	name = instance.space.name
	from datetime import date
	today = date.today()
	today_path = today.strftime("%Y/%m/%d")
	return "decorate_space/%s/%s-%s"%(name,today_path,filename)


class DecorateSpace(models.Model):
	name = models.CharField(max_length=156)
	email = models.EmailField(max_length=256)
	phone_number = models.CharField(max_length=12)
	address = models.CharField(max_length=500)
	message = models.TextField(max_length=1256)

	def __str__(self):
		return self.name

class DecorateSpaceImage(models.Model):
	space = models.ForeignKey(DecorateSpace, related_name="image")
	image = models.ImageField(upload_to=get_space_image_name, verbose_name='Image', blank=True, null=True )

	def __str__(self):
		return self.space.name

	def save(self, *args, **kwargs):
		cloudinary.uploader.upload( self.image, folder=get_space_image_name, public_id=os.path.splitext(self.image.name)[0])

		super(DecorateSpaceImage, self).save(*args, **kwargs)

