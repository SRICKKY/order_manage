from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Order
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	return render(request, 'myapp/index.html')

@login_required
def order(request):
	order = Order.objects.all()
	return render(request, 'myapp/order.html', {'order': order})

def signup(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request, user)
			return redirect('/login')
	else:
		form = UserCreationForm()


	return render(request, 'registration/signup.html',{'form':form})


@login_required
def order(request):
	orders = Order.objects.filter(name=request.user)
	return render(request, 'myapp/order.html',{'orders': orders})

@login_required
def details(request, pk):
	order = Order.objects.get(id=pk)
	return render(request, 'myapp/details.html', {'order': order})

@login_required
def add(request):

	if request.method == 'POST':
		form = OrderForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['customer_name']
			item = form.cleaned_data['item']
			quantity = form.cleaned_data['quantity']
			rate = form.cleaned_data['rate']
			total = form.cleaned_data['total']

			Order.objects.create(name=name,item=item,quantity=quantity,rate=rate,total=total).save()

			return HttpResponseRedirect('/')
	else:
		form = OrderForm()

	return render(request, 'myapp/form.html',{'form':form})

@login_required
def delete(request, pk):
	if request.method == 'DELETE':
		order = get_object_or_404(Entry,pk=pk)
		order.delete()
		
	return HttpResponseRedirect('/order')

