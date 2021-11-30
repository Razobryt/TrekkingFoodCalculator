from django.contrib import admin
from .models import Product, Customer, CartProduct, Cart


class AdminUser(admin.ModelAdmin):
	list_display = ('username', 'is_staff', 'is_active')
	readonly_fields = ('username', 'last_login')
	list_filter = ('is_staff',)
	search_fields = ('username',)
	fieldsets = (
		(
			None,
			{
				'fields': (
					'username',
					'password',
					'is_staff',
					'last_login',
					)
				},
			),
		)


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)
