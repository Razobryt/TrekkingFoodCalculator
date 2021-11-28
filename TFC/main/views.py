from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .forms import CreateUserForm, Hike
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')


def calculator(request):
	form = Hike()
	table = Product.objects.all()

	if request.method == 'POST':
		form = Hike(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/calculator.html')
	context = {'form': form, 'products': table}
	return render(request, 'main/calculator.html', context)


def new(request):
	return render(request, 'main/new.html')


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
