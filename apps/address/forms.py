from django import forms
from oscar.apps.address.forms import UserAddressForm as CoreUserAddressForm

class UserAddressForm(CoreUserAddressForm):
	state = forms.CharField(
			widget = forms.TextInput(attrs={'placeholder': 'Telangana'}),
            disabled=True,
            required = False
        )

