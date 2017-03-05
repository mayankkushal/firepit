from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Store(models.Model):
	name = models.CharField(_('Name'), max_length=255, db_index=True)
	description = models.TextField(_('Description'), blank=True)
	image = models.ImageField(_('Image'), upload_to='stores', blank=True, null=True, max_length=255)
	slug = models.SlugField(_('Slug'), max_length=255, db_index=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Store, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Product(AbstractProduct):
	store = models.ForeignKey(Store, related_name='product', null=True)



# wierd, but it should be here. Loading all oscar models
from oscar.apps.catalogue.models import *  # noqa