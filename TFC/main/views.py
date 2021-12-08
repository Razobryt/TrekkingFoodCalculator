from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartProduct, User
from .forms import SignInForm, LogInForm, HikeForm, CartForm


def index(request):
	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')


def calculator(request):
	form = HikeForm()
	products = Product.objects.all()
	cart = CartForm(request.POST, )
	if request.method == 'POST':
		form = HikeForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/calculator.html')
	context = {'form': form, 'products': products, 'cart': cart}
	return render(request, 'main/calculator.html', context)


@login_required(login_url='login')
def cart_add(request):
	user = User.objects.get(user=request.user)
	cart = Cart.objects.get(owner=user)
	product = Product.objects.get(id=request.product_id)
	cart_product = CartProduct.objects.create(
		user=user, cart=cart, product=product
		)
	cart.products.add(cart_product)
	return render(request, 'main/calculator.html')


def log_in_user(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = LogInForm()
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Имя пользователя или пароль не верны')
		context = {'form': form}
		return render(request, 'main/login.html', context)


@login_required(login_url='login')
def logout_user(request):
	logout(request)
	return redirect('home')


def signin_user(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = SignInForm()

		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, f'{user} был успешно создан')
				return redirect('login')
			else:
				messages.error(request, )

		context = {'form': form}
		return render(request, 'main/sign_in.html', context)


def userprofile(request):
	return render(request, 'main/userprofile.html')
