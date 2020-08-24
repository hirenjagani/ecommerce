from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CartAddProductForm

from product.models import Product
from .cart import Cart

@require_POST
@login_required
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'carthome.html', {'cart': cart})






#........................................

# @login_required
# def cart_home(request):
#
#     # cart_obj, new_obj = Cart.objects.new_or_get(request)
#     # products = cart_obj.products.all()
#     # total = 0
#     # for x in products:
#     #     total += x.price
#     # print(total)
#     # cart_obj.total = total
#     # cart_obj.save()
#     return render(request, "carthome.html", {})
#
#
# def cart_update(request):
#     product_id = request.POST.get('product_id')
#     if product_id is not None:
#         try:
#             product_obj = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             print("Show message to user, product is gone?")
#             return redirect("cart:home")
#         cart_obj, new_obj = Cart.objects.new_or_get(request)
#         if product_obj in cart_obj.products.all():
#             cart_obj.products.remove(product_obj)
#         else:
#             cart_obj.products.add(product_obj)  # cart_obj.products.add(product_id)
#
#         # return redirect(product_obj.get_absolute_url())
#
#
#     return redirect("cart:home")