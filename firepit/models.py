from django.db import models

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
