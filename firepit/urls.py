from django.conf.urls import url
from firepit import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'catalogue/store/(?P<store_slug>[\w\-]+)', views.store, name='store'),
	url(r'request_quote', views.request_quote, name='request_quote'),
	url(r'decorate_space', views.decorate_space, name='decorate_space'),
	url(r'thank_you', views.thank_you, name='thank_you')
]