from django.conf.urls import url
from firepit import views

urlpatterns = [
	url(r'^$', views.index, name="index")
]