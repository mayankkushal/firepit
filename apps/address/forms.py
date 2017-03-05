from django import forms
from oscar.apps.address.forms import AbstractAddressForm

class UserAddressForm(AbstractAddressForm):
	exclude = ['country']

from oscar.apps.address.forms import *