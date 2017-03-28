from oscar.apps.basket.forms import AddToBasketForm as CoreAddToBasketForm
from django import forms

class AddToBasketForm(CoreAddToBasketForm, forms.Form):

	def _create_parent_product_fields(self, product):

		self.fields['child_id'] = forms.ChoiceField(
			choices=tuple(choices), label=_("Variants"),
			widget=widgets.RadioSelect())