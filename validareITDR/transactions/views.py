from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dashboard.models import Product
from .models import Sales
from .forms import TestClass
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers

from django.shortcuts import HttpResponse


@login_required
def transactions(request):
    product_list = Product.objects.all()
    if request.method == 'POST':
        bon = TestClass(request.POST)
        if bon.is_valid():
            bill = bon.cleaned_data['bon_no']
            print('*' * 15)
            print(bill)
            print('*' * 15)

    else:
        bon = TestClass(initial={'Numar Bon': 5})
        context = {
            'product_list': product_list,
            'bon': bon
        }

    print('*' * 15)
    print(bon)
    print('*' * 15)

    return render(request, 'transactions.html', context)


def ajax_response(request):
    ticket = request.GET.get('ticket')
    data = {
        'is_taken': Sales.objects.filter(ticket_no__iexact=ticket).exists()
    }
    return JsonResponse(data)



