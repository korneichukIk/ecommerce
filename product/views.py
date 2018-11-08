from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def list_view(request, category_slug = None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)

    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }
    return render(request, 'list.html', context)

def detail_view(request, category_slug, slug):
    product = get_object_or_404(Product, slug = slug, category__slug = category_slug)
    categories = Category.objects.all()

    context = {'product': product,
               'categories': categories
    }
    return render(request, 'detail.html', context)
