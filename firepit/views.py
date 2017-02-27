from django.shortcuts import render
from oscar.apps.catalogue.models import Category
from .models import SlideShowImage, Banner

# Create your views here.

def index(request):
	image_list = SlideShowImage.objects.filter(slideshow=Banner.objects.get(name='slideshow'))
	category_list = Category.objects.all()
	return render(request, 'firepit/index.html', {'category_list':category_list, 'image_list':image_list} )