from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51TMpI0PZ9NrZzLBuMowYIu4ILA4XGtvhXkW22kRmQgsgAkxNY963Uv298KJ7E2KNtTLfjX3gXT8ypITrjt8UbU1Z00jkpgXIXR',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)