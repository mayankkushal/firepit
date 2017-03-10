from django import template
from apps.catalogue.models import Store

register = template.Library()

@register.assignment_tag
def store_list():
	return Store.objects.all().order_by('-views')