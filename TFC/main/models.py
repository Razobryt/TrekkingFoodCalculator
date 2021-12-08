from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Нужно расширить Пользователя... скорее всего придётся создавать класс и наследовать его от АбстрактногоЮзера...
# Для того чтобы можно было сделать отображение всей истории созданных походов...
# И скорее всего отказавшись от модели Customer не имеет смысла модель CartProduct... переопределить на модель
# Product...

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255, db_index=True, verbose_name='Название продукта')
	slug = models.SlugField(max_length=200, unique=True, db_index=True)
	weight = models.PositiveIntegerField(default=100, blank=False, verbose_name='Порция')
	calories = models.PositiveIntegerField(default=2500, blank=False, verbose_name='Калорийность в 100г')

	def __str__(self):
		return self.title


# class Customer(models.Model):
# 	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return 'Пользователь: {}'.format(self.user.name)


class CartProduct(models.Model):
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
	product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
	max_weight = models.PositiveIntegerField(verbose_name='Вес раскладки')
	max_calories = models.PositiveIntegerField(verbose_name='Получено калорий')

	def __str__(self):
		return 'Продукт: {} '.format(self.product.title)

	def save(self, *args, **kwargs):
		self.max_weight += Product.weight
		self.max_calories += Product.calories
		super().save(*args, **kwargs)


class Cart(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название похода')
	comment = models.TextField(blank=True, verbose_name='Комментарий')
	number_of_persons = models.PositiveIntegerField(default=1, blank=False, verbose_name='Количество человек')
	number_of_days = models.PositiveIntegerField(default=1, blank=False, verbose_name='Продолжительность похода')
	calories_per_day = models.PositiveIntegerField(default=2500, blank=False, verbose_name='Калорий в сутки')
	max_weight = models.PositiveIntegerField(default=0, verbose_name='Вес раскладки')
	max_calories = models.PositiveIntegerField(default=0, verbose_name='Получено калорий')
	owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)
	products = models.ManyToManyField(CartProduct, blank=True, verbose_name='Продукты', related_name='related_cart')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.max_weight += CartProduct.max_weight
		self.max_calories += CartProduct.max_calories
		super().save(*args, **kwargs)
