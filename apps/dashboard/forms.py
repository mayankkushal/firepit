from django import forms
from apps.catalogue.models import Store, Product
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm

class ProductForm(CoreProductForm):
    class Meta(CoreProductForm.Meta):
        model = Product
        fields = ['title','store', 'upc', 'description', 'is_discountable', 'structure']


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'image', 'slug')




