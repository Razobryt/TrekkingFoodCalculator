from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cart
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class Hike(ModelForm):
	class Meta:
		model = Cart
		fields = ['title', 'number_of_days', 'number_of_persons', 'calories_per_day']
