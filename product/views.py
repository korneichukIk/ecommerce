from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from product.models import Product, Category
from .forms import cart_add_form
from django.views.decorators.http import require_POST

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
    cart_product_form = cart_add_form()

    context = {'product': product,
               'categories': categories,
               'cart_add_form': cart_product_form,
    }
    return render(request, 'detail.html', context)

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = cart_add_form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_to_cart(product=product, amount=cd['amount'],
                         update_amount=cd['update'])

    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_amount_form'] = cart_add_form(
            initial={
                'amount': item['amount'],
                'update': True
            }
        )

    context = {'cart': cart}
    return render(request, 'cart_detail.html', context)

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove_from_cart(product)
    return redirect('cart')
