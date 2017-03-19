from django import template
from oscar.apps.basket.models import Basket
from instamojo_wrapper import Instamojo
from oscar.core.loading import get_class, get_classes, get_model
from oscar.apps.checkout.views import PaymentDetailsView
from django.template import Context, RequestContext

Order = get_model('order', 'Order')
Basket = get_model('basket', 'Basket')
#Checkout = get_model('checkout', 'Checkout')
OrderNumberGenerator = get_class('order.utils', 'OrderNumberGenerator')
CheckoutSessionData = get_class('checkout.utils', 'CheckoutSessionData')
OrderPlacementMixin = get_class('checkout.mixins', 'OrderPlacementMixin')
OrderCreator = get_class('order.utils', 'OrderCreator')

register = template.Library() 

@register.simple_tag(takes_context=True)
def success(context):
	request = context['request']
	order_number = request.session['order_number']
	'''#basket = context['basket']
	#print(basket)
	shipping_charge = context['shipping_charge']
	shipping_address = context['shipping_address']
	shipping_method = context['shipping_method']
	user = request.user 
	CheckoutSessionData(request).set_order_number(order_number)
	OrderPlacementMixin().freeze_basket(basket)
	CheckoutSessionData(request).set_submitted_basket(basket)

	OrderPlacementMixin().place_order(order_number, user, basket, shipping_address,
                    shipping_method, shipping_charge, order_total,
                    )
	order_done = Order.objects.get(nember=order_number)'''
	print(order_number)
	return context['basket']
