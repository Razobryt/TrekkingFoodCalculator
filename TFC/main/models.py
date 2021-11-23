from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название продукта')
	weight = models.PositiveIntegerField(blank=False, verbose_name='Вес')
	calories = models.PositiveIntegerField(blank=False, verbose_name='Калорийность')

	def __str__(self):
		return self.name


class Customer(models.Model):
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

	def __str__(self):
		return 'Пользователь: {}'.format(self.user.name)


class CartProduct(models.Model):
	user = models.ForeignKey(Customer, verbose_name='Пользователь', on_delete=models.CASCADE)
	cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
	product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
	qty = models.PositiveIntegerField(default=100)
	max_weight = models.PositiveIntegerField(verbose_name='Вес раскладки')
	max_calories = models.PositiveIntegerField(verbose_name='Получено калорий')

	def __str__(self):
		return 'Продукт: {} '.format(self.product.name)


class Cart(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название похода')
	comment = models.TextField(blank=True, verbose_name='Коментарий')
	number_of_days = models.PositiveIntegerField(blank=False, verbose_name='Продолжительность похода')
	calories_per_day = models.PositiveIntegerField(default=2500, verbose_name='Калорий в сутки')
	max_weight = models.PositiveIntegerField(verbose_name='Вес раскладки')
	max_calories = models.PositiveIntegerField(verbose_name='Получено калорий')
	owner = models.ForeignKey(Customer, verbose_name='Владелец', on_delete=models.CASCADE)
	products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')

	def __str__(self):
		return self.title
