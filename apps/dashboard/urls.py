from django.conf.urls import url
from apps.dashboard import views

app_name = 'dashboard'
urlpatterns = [
	url(r'^store_list', views.store_list, name="store_list"),
	url(r'^store_add', views.store_add, name="store_add"),
	url(r'^store_delete/(?P<pk>[\w\-]+)', views.store_delete, name="store_delete")
]