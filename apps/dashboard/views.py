from django.shortcuts import render,redirect
from apps.dashboard.forms import StoreForm
from apps.catalogue.models import Store
from django_tables2 import RequestConfig
from apps.dashboard.tables import StoreTable

def store_list(request):
	store = StoreTable(Store.objects.all())
	RequestConfig(request).configure(store)
	return render(request, 'dashboard/store_list.html', {'store':store})

def store_add(request):
	if request.method == "POST":
		store_form = StoreForm(request.POST)
		if store_form.is_valid():
			image = request.FILES['image']
			store = store_form.save(commit=False)
			store.image = image
			store.save()
			return redirect('/dashboard/store_list')
	else:
		store_form = StoreForm()
		return render(request, 'dashboard/store_form.html', {'store_form':store_form} )

def store_delete(request, pk):
	if request.method == 'POST':
		store = Store.objects.get(pk=pk)
		store.delete()
		return redirect('/dashboard/store_list') 
	else:
		store = Store.objects.get(pk=pk)
		return render(request, 'dashboard/store_delete.html', {'store':store})

def store_update(request, pk):
	instance = Store.objects.get(pk=pk)
	store_form = StoreForm(request.POST or None, instance=instance)
	if store_form.is_valid():
		store_form.save()
		return redirect('/dashboard/store_list')
	else:
		return render(request, 'dashboard/store_update.html', {'store_form':store_form, 'store':instance})