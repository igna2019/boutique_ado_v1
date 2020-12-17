from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hz3gLFW5nLHB4CRVM0LWwvYDxaOjc6iop7IVII4kNrYZbHy8ZMVyEV3iw7kI3L1uoLjv88HjTi9tIhm0qyqRZzk00TFb51s9J',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)