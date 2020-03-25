from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    title = 'Order Summary'
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order, 'title': title})
    else:
        form = OrderCreateForm()
        title = 'Order Summary'
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'title': title})
