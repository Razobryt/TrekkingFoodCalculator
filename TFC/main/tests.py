from django.test import TestCase
from .models import CartProduct, Cart, Product
from django.contrib.auth import get_user_model

User = get_user_model()


class CalcTest(TestCase):
	def setUp(self) -> None:
		self.user = User.objects.create(username='testuser', password='password')
		# self.customer = Customer.objects.create(user=self.user, address='Address')
		self.product = Product.objects.create(title='test', slug='test-slug', weight='60', calories='200')
		self.cart = Cart.objects.create(owner=self.user)
		self.cartproduct = CartProduct.objects.create(user=self.user, cart=self.cart)

	def test_add_to_cart(self):
		self.cart.products.add(self.cartproduct)
		self.assertIn(self.cartproduct, self.cart.products.all())
		self.assertEqual(self.cart.products.count(), 1)
