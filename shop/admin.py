from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['available', 'special_offer', 'bestseller']
    list_display = ['name', 'category', 'price',
                    'available', 'special_offer',
                    'bestseller', 'slug']
    list_editable = ['price', 'available', 'special_offer', 'bestseller', 'category']
    prepopulated_fields = {'slug': ('name',)}
