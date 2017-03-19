from oscar.apps.search.search_indexes import *
from apps.catalogue.models import Store

class StoreIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(
        document=True, use_template=True,
        template_name='search/indexes/store/store_text.txt')
	name = indexes.CharField(model_attr='name')
	description = indexes.CharField(model_attr='description')
	rendered = indexes.CharField(use_template=True, indexed=False)

	def get_model(self):
		return Store

	def index_queryset(self, using=None):
		return self.get_model().objects.all()