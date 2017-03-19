from django import template
from oscar.apps.analytics.models import ProductRecord
from oscar.core.loading import get_class

BasketVoucherForm = get_class('basket.forms', 'BasketVoucherForm')

register = template.Library()

@register.assignment_tag
def voucher_form_from_tag():
	voucher_form = BasketVoucherForm()
	return voucher_form
