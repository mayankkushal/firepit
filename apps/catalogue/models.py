from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductImage, AbstractCategory
import cloudinary
import os
from django.conf import settings
from django.urls import reverse
from datetime import date, datetime

class Store(models.Model):
	name = models.CharField(_('Name'), max_length=255, db_index=True)
	description = models.TextField(_('Description'), blank=True)
	image = models.ImageField(_('Image'), upload_to='stores', blank=True, null=True, max_length=255)
	slug = models.SlugField(_('Slug'), max_length=255, db_index=True)
	views = models.PositiveIntegerField(_('Views'))

	def get_absolute_url(self):
		return '/catalogue/store/%s'% self.slug

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		cloudinary.uploader.upload( self.image, folder='stores', public_id=os.path.splitext(self.image.name)[0])
		super(Store, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Product(AbstractProduct):
	store = models.ForeignKey(Store, related_name='product', null=True)

class ProductImage(AbstractProductImage):
	def save(self, *args, **kwargs):
		cloudinary.uploader.upload( self.original, folder=settings.OSCAR_IMAGE_FOLDER, public_id=os.path.splitext(self.original.name)[0])
		super(ProductImage, self).save(*args, **kwargs)

class Category(AbstractCategory):
	def save(self, *args, **kwargs):
		cloudinary.uploader.upload( self.image, folder='categories', public_id=os.path.splitext(self.image.name)[0])
		super(Category, self).save(*args, **kwargs)


# wierd, but it should be here. Loading all oscar models
from oscar.apps.catalogue.models import *  # noqa