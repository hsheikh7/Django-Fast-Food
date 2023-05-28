from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart2.forms import CartAddProductForm
from .cart import Cart
from website.models import Menu


#@require_POST
def cart_add(requset, product_id):
    cart = Cart(requset)
    product = get_object_or_404(Menu, id=product_id)
    cart.add(product=product)
    return redirect('/')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    cart.remove(product)
    return redirect('/')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/")

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = CartAddProductForm(
            initial={'product_count': item['product_count'],
                     'update': True})
    return render(request, 'index.html', {'cart': cart})

    