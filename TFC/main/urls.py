from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('calculator', views.calculator, name='calculator'),
	path('login', views.log_in_user, name='login'),
	path('logout', views.logout_user, name='logout'),
	path('signin', views.signin_user, name='signin'),
	path('cart_add', views.cart_add, name='cart_add'),
	]
