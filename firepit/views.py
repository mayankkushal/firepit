from django.shortcuts import render
from .models import SlideShowImage, Banner, RequestQuote, RequestQuoteImage, DecorateSpaceImage, DecorateSpace
from apps.catalogue.models import Product, Store
from .forms import RequestQuoteForm, RequestQuoteImageForm, DecorateSpaceForm, DecorateSpaceImageForm, PowerSolutionForm
from django.forms import BaseModelFormSet
from django.forms.models import modelformset_factory
from oscar.apps.order.models import Order
from oscar.core.loading import get_class, get_classes, get_model
from django.template import RequestContext, Context


OrderPlacementMixin = get_class('checkout.mixins', 'OrderPlacementMixin')
Basket = get_model('basket', 'basket')
Order = get_model('order', 'Order')
CheckoutSessionData = get_class('checkout.utils', 'CheckoutSessionData')
BasketMiddleware = get_class('basket.middleware', 'BasketMiddleware')
Selector = get_class('partner.strategy', 'Selector')

# Create your views here.

def index(request):
	image_list = SlideShowImage.objects.filter(slideshow=Banner.objects.get(name='slideshow'))
	category_list = Category.objects.all()
	return render(request, 'firepit/index.html', {'category_list':category_list, 'image_list':image_list} )


def store(request, store_slug):
	store = Store.objects.get(slug=store_slug)
	store.views += 1
	store.save()
	product_list = Product.objects.filter(store=store)
	count = Product.objects.filter(store=store).count()
	context_dict = {'product_list':product_list, 'store_cur':store, 'count':count}
	return render(request, 'catalogue/store.html', context_dict)

def request_quote(request):
	ImageFormSet = modelformset_factory(RequestQuoteImage, form=RequestQuoteImageForm, extra=5)#extra can be increased for more no 
	if request.method == 'POST':																# of images
		quote_form = RequestQuoteForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES,
                               queryset=RequestQuoteImage.objects.none())
		if quote_form.is_valid() and formset.is_valid():
			quote = quote_form.save(commit=False)
			if request.user.is_authenticated():
				quote.name = request.user.first_name
				quote.email = request.user.email
			quote.save()
			for form in formset.cleaned_data:
				try:
					image = form['image']
				except KeyError:
					image = None
				if image:
					photo = RequestQuoteImage(quote=quote, image=image)
					photo.save()
			return render(request, 'firepit/success.html', {'total':total})
		else:
			print(quote_form.errors, formste.errors)
	else:
		quote_form = RequestQuoteForm()
		formset = ImageFormSet(queryset=RequestQuoteImage.objects.none())
	return render(request, 'firepit/request_quote.html',{'quote_form':quote_form, 'formset':formset})

def thank_you(request):
	
	order_number = request.session['order_number']
	BasketMiddleware().process_request(request)
	basket = Basket.objects.get(pk=request.session['basket'])
	shipping_address = request.session['shipping_address']
	shipping_method = request.session['shipping_method']
	shipping_charge = request.session['shipping_charge']
	order_total = request.session['order_total']
	user = request.user
	CheckoutSessionData(request).set_order_number(order_number)
	OrderPlacementMixin().freeze_basket(basket)
	CheckoutSessionData(request).set_submitted_basket(basket)
	basket.strategy = Selector().strategy(request, user=request.user)
	print(basket.strategy)
	try:
		OrderPlacementMixin().place_order(order_number=order_number, user=user, basket=basket, shipping_address=shipping_address,
                    shipping_method=shipping_method, shipping_charge=shipping_charge, order_total=order_total,
                    )  
	except ValueError:
		pass
	order = Order.objects.get(number=order_number)
	              
	return render(request, 'thank_you.html', {"order":order})

def decorate_space(request):
	ImageFormSet = modelformset_factory(DecorateSpaceImage, form=DecorateSpaceImageForm, extra=5)#extra can be increased for more no 
	if request.method == 'POST':																# of images
		space_form = DecorateSpaceForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES,
                               queryset=DecorateSpaceImage.objects.none())
		if space_form.is_valid() and formset.is_valid():
			space = space_form.save(commit=False)
			if request.user.is_authenticated():
				space.name = request.user.first_name
				space.email = request.user.email
			space.save()
			for form in formset.cleaned_data:
				try:
					image = form['image']
				except KeyError:
					image = None
				if image:
					photo = DecorateSpaceImage(space=space, image=image)
					photo.save()
			return render(request, 'firepit/success.html', {'total':total})
		else:
			print(space_form.errors, formset.errors)
	else:
		space_form = DecorateSpaceForm()
		formset = ImageFormSet(queryset=DecorateSpaceImage.objects.none())
	return render(request, 'firepit/decorate_space.html',{'space_form':space_form, 'formset':formset})
	
def power_solution(request):
	total = 0
	if request.method == "POST":
		sol_form = PowerSolutionForm(request.POST)
		if sol_form.is_valid():
			sol = sol_form.save()
			return render(request, 'firepit/success.html')
	else:
		sol_form = PowerSolutionForm()
		return render(request, 'firepit/power_solution.html', {'sol_form':sol_form}) 
