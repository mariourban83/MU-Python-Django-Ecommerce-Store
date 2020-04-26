from django.shortcuts import render
from cart.cart import Cart
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_options(request):
    title = 'LR | Checkout options'
    return render(request, 'payments/checkout_options.html',
                  {'title': title})


def payment(request):
    title = 'LR | Payment'
    cart = Cart(request)
    total_price = cart.get_total_price()
    CLIENT_ID = settings.CLIENT_ID  # Paypal
    pubKey = settings.STRIPE_PUBLISHABLE_KEY  # Stripe
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=int(total_price * 100),
            currency='EUR',
            source=request.POST['stripeToken']
        )
        print(request.POST)
        print(charge)
        cart.clear()
        return render(request, 'payments/payment_success.html',
                      {'pubKey': pubKey})
    return render(request, 'payments/payment.html',
                  {'title': title,
                   'cart': cart,
                   'total_price': total_price,
                   'CLIENT_ID': CLIENT_ID,
                   'pubKey': pubKey})


def payment_success(request):
    title = 'LR | Payment Success'
    return render(request, 'payments/payment_success.html',
                  {'title': title})
