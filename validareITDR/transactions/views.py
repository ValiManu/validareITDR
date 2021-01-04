from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.datetime_safe import datetime

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
    context = {
          'product_list': product_list
    }

    return render(request, 'transactions.html', context)


def ajax_response(request):
    ticket = request.GET.get('ticket')
    data = {
        'is_taken': Sales.objects.filter(ticket_no__iexact=ticket).exists()
    }
    if data['is_taken']:
        pass

    print('*' * 15)
    print(ticket)
    print('*' * 15)
    return JsonResponse(data)



