from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {
        'slug': ['title']
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'image', 'short_description', 'description', 'price', 'stock', 'created', 'updated', 'available']
    list_editable = ['price', 'stock', 'available']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {
        'slug': ['title']
    }
