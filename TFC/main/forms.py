from django.contrib.auth import authenticate, login as log_in
from django.forms import ModelForm
from django import forms
from .models import Cart, User


# from django.contrib.auth.models import User


class SignInForm(forms.Form):
	username = forms.CharField(
		label="Имя пользователя",
		widget=forms.TextInput(
			attrs={
				"id": "name",
				"class": "form-control",
				"placeholder": "Имя пользователя",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Имя пользователя'",
				}
			),
		)
	email = forms.EmailField(
		label="Адрес электронной почты",
		widget=forms.TextInput(
			attrs={
				"id": "email",
				"class": "form-control",
				"placeholder": "Электронный адрес",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Электронный адрес'",
				}
			),
		)
	password = forms.CharField(
		label="Пароль",
		widget=forms.PasswordInput(
			attrs={
				"id": "password",
				"class": "form-control",
				"placeholder": "Пароль",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Пароль'",
				}
			),
		)
	repeat_password = forms.CharField(
		label="Подтверждение пароля",
		widget=forms.PasswordInput(
			attrs={
				"id": "repeat_password",
				"class": "form-control",
				"placeholder": "Повторите пароль",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Повторите пароль'",
				}
			),
		)

	def clean(self):
		is_error = False
		try:
			tmp_user = User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			...
		else:
			self.add_error('username', 'Такой пользователь уже существует.')
			is_error = True
		if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
			self.add_error('password', 'Пароли не совпадают.')
			self.add_error('repeat_password', 'Пароли не совпадают.')
			is_error = True
		return super().clean()

	def save(self):
		new_user = User(
			username=self.cleaned_data['username'],
			email=self.cleaned_data['email'],
			password=self.cleaned_data['password'],
			)

		new_user.save()


class LogInForm(forms.Form):
	username = forms.CharField(
		label="Имя пользователя",
		widget=forms.TextInput(
			attrs={
				"id": "name",
				"class": "form-control",
				"placeholder": "Имя пользователя",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Имя пользователя'",
				}
			),
		)
	password = forms.CharField(
		label="Пароль",
		widget=forms.PasswordInput(
			attrs={
				"id": "password",
				"class": "form-control",
				"placeholder": "Пароль",
				"onfocus": "this.placeholder = ''",
				"onblur": "this.placeholder = 'Пароль'",
				}
			),
		)

	def clean(self):
		user = authenticate(**dict(self.cleaned_data))
		if user is not None:
			self.user = user
			return self.cleaned_data
		else:
			self.add_error('username', 'invalid username.')
			self.add_error('password', 'or invalid password.')
			raise forms.ValidationError('User not found!')

	def login(self, request):
		log_in(request, self.user)


class HikeForm(ModelForm):
	class Meta:
		model = Cart
		fields = ['title', 'number_of_days', 'number_of_persons', 'calories_per_day']


class CartForm(ModelForm):
	class Meta:
		model = Cart
		fields = ['products', 'max_weight', 'max_calories']
