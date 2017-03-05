from django import template
from ..models import Store

register = template.Library()

@register.simple_tag
def store_list():
	store_list = Store.objects.get()
	return store_list


@register.simple_tag
def store_count():
	count = Store.objects.all().count()
	return count