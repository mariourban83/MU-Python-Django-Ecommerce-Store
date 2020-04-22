from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout_options', views.checkout_options, name='checkout_options'),
    path('payment', views.payment, name='payment'),
    path('payment_success', views.payment_success, name='payment_success')
]
