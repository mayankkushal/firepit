from django.shortcuts import render
from .models import SlideShowImage, Banner, RequestQuote, RequestQuoteImage, DecorateSpaceImage, DecorateSpace
from apps.catalogue.models import Product, Store
from .forms import RequestQuoteForm, RequestQuoteImageForm, DecorateSpaceForm, DecorateSpaceImageForm
from django.forms import BaseModelFormSet
from django.forms.models import modelformset_factory
from oscar.apps.order.models import Order
from oscar.core.loading import get_class, get_classes, get_model
from django.template import RequestContext, Context


OrderPlacementMixin = get_class('checkout.mixins', 'OrderPlacementMixin')
Basket = get_model('basket', 'Basket')
CheckoutSessionData = get_class('checkout.utils', 'CheckoutSessionData')

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
		else:
			print(quote_form.errors, formste.errors)
	else:
		quote_form = RequestQuoteForm()
		formset = ImageFormSet(queryset=RequestQuoteImage.objects.none())
	basket = Basket.objects.get(pk=request.session['basket'])
	print(basket)
	return render(request, 'firepit/request_quote.html',{'quote_form':quote_form, 'formset':formset})

def thank_you(request):
	
	order_number = request.session['order_number']
	order = Order.objects.get(number=order_number)                 
	return render(request, 'checkout/thank_you.html', {'order':order})

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
		else:
			print(space_form.errors, formset.errors)
	else:
		space_form = DecorateSpaceForm()
		formset = ImageFormSet(queryset=DecorateSpaceImage.objects.none())
	return render(request, 'firepit/decorate_space.html',{'space_form':space_form, 'formset':formset})
	