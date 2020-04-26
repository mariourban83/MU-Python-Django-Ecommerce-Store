from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
import weasyprint
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def order_create(request):
    cart = Cart(request)
    title = 'Order Summary'
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print(form)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            orders = Order.objects.all()
            user = get_user_model()
            user.objects.all()
            users = User.objects.all()
            return redirect(reverse('payments:payment'),
                            {'order': order, 'title': title,
                             'orders': orders,
                             'users': users},)
    else:
        form = OrderCreateForm()
        title = 'Order Summary'
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'title': title})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order_pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(
                                      order.id)
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(
                                                        'static/css/pdf.css')])
    return response
