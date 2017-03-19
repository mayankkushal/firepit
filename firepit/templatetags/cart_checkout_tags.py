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

api = Instamojo(api_key='e592148daf8eae546e01e6b2f18ad1fb',
                auth_token='9e09a975978993c860602dcef3ec76f3')

register = template.Library() 

@register.simple_tag(takes_context=True)
def checkout_url(context):
	request = context['request']
	order_total = context['order_total']
	basket = context['basket']
	shipping_charge = context['shipping_charge']
	shipping_address = context['shipping_address']
	shipping_method = context['shipping_method']

	request.session['shipping_address'] = shipping_address
	request.session['shipping_method'] = shipping_method
	request.session['shipping_charge'] = shipping_charge
	request.session['basket'] = basket.pk
	request.session['order_total'] = order_total
	
	user = request.user
	order_number = OrderNumberGenerator().order_number(basket)
	request.session['order_number'] = order_number
	print(order_number)
	phone = shipping_address.phone_number.as_national
	response = api.payment_request_create(
			amount=order_total.incl_tax,
			buyer_name=request.user.first_name,
			purpose=order_number,
			send_email=False,
			email=request.user.email,
			redirect_url="https://firepit.in/thank_you",# thank_you view will be called
			phone= phone
		)
	url = response['payment_request']['longurl']
	return url


