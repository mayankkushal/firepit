from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from django.shortcuts import redirect

class ShippingMethodView(CoreShippingMethodView):

	def get_success_response(self):
		return redirect('checkout:payment-details')


class PaymentDetailsView(CorePaymentDetailsView):

	preview = True