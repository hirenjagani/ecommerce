from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart
from .models import Order,OrderItem
# Create your views here.

def order_create(request):

    cart = Cart(request)

    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=Order.objects.create(
                user=request.user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email= form.cleaned_data.get('email'),
                address=form.cleaned_data.get('address'),
                phone_no=form.cleaned_data.get('phone_no'),
                pin_code=form.cleaned_data.get('pin_code'),
                created=form.cleaned_data.get('created'),
                city=form.cleaned_data.get('city'),
                updated=form.cleaned_data.get('updated'),
            )
            for item in cart:
              OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
              )
              cart.clear()
        return render(request,'cartcreated.html',{'order':order})
    else:
        form=OrderForm()
    return render(request,'cartcreate.html',{'form':form,'cart':cart})


def my_orders(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    return render(request,'myorders.html',{'orders':orders})
