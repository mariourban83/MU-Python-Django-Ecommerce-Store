from django.shortcuts import render
from cart.cart import Cart



def checkout_options(request):
    title = 'LR | Checkout options'
    return render(request, 'payments/checkout_options.html',
                  {'title': title})


def payment(request):
    title = 'LR | Payment'
    cart = Cart(request)
    print(cart)
    return render(request, 'payments/payment.html',
                  {'title': title})
