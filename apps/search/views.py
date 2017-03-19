from oscar.apps.search.views import FacetedSearchView as CoreFacetedSearchView
from apps.catalogue.models import Store
from apps.catalogue.models import Product

class FacetedSearchView(CoreFacetedSearchView):

	def get_results(self):
		return super(FacetedSearchView, self).get_results().models(Product, Store)


