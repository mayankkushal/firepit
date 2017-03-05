from django import template
from firepit.models import SlideShowImage, Banner

register = template.Library()

@register.assignment_tag
def image_list():
	image_list = SlideShowImage.objects.filter(slideshow=Banner.objects.get(name='slideshow'))
	return image_list