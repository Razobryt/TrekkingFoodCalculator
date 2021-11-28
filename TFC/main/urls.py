from django.urls import path
from . import views
# from .views import logout

urlpatterns = [
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('calculator', views.calculator, name='calculator'),
	path('new', views.new, name='new'),
	path('login', views.log_in_user, name='login'),
	path('logout', views.logout_user, name='logout'),
	path('signin', views.signin_user, name='signin'),
	# path('logout', logout, name='logout')
	]
