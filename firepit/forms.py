from django import forms
from .models import RequestQuote, RequestQuoteImage, DecorateSpace, DecorateSpaceImage, PowerSolutions


class RequestQuoteForm(forms.ModelForm):
	class Meta:
		model = RequestQuote
		fields = ['name', 'email', 'phone_number', 'message']

class RequestQuoteImageForm(forms.ModelForm):
	class Meta:
		model = RequestQuoteImage
		fields = ['image']
		
class DecorateSpaceForm(forms.ModelForm):
	class Meta:
		model = DecorateSpace
		fields = ['name', 'email', 'address', 'phone_number', 'message']

class DecorateSpaceImageForm(forms.ModelForm):
	class Meta:
		model = DecorateSpaceImage
		fields = ['image']

class PowerSolutionForm(forms.ModelForm):
	class Meta:
		model = PowerSolutions
		fields = '__all__'