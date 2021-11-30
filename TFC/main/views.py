from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Customer, CartProduct
from .forms import CreateUserForm, Hike


def index(request):
	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')


def calculator(request):
	form = Hike()
	products = Product.objects.all()
	cart = Cart(request)

	if request.method == 'POST':
		form = Hike(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/calculator.html')
	context = {'form': form, 'products': products, 'cart': cart}
	return render(request, 'main/calculator.html', context)


@login_required(login_url='login')
def cart_add(request):
	cart = Cart(request)
	product = get_object_or_404(Product, id='product_id')
	cart.add(products=product)
	return redirect('cart:calculator')


def log_in_user(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Имя пользователя или пароль не верны')
		return render(request, 'main/login.html')


@login_required(login_url='login')
def logout_user(request):
	logout(request)
	return redirect('home')


def signin_user(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, f'{user} был успешно создан')
				return redirect('login')

		context = {'form': form}
		return render(request, 'main/sign_in.html', context)
