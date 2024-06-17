from django.contrib import admin

from products.models import Category, Product, Review, About

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(About)
