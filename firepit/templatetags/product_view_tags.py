from django import template
from oscar.apps.analytics.models import ProductRecord

register = template.Library()

@register.assignment_tag
def product_record():
	product_list = ProductRecord.objects.all().order_by('-num_views')[:4]
	print(product_list)
	return product_list