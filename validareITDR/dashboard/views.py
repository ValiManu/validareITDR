from datetime import datetime
from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from transactions.models import Sales
from .models import Shop, Prize
from django.shortcuts import HttpResponse


@login_required
def index(request):
    shop = get_object_or_404(Shop.objects.filter(user__exact=request.user.id))
    prize_list = Prize.objects.filter(shop__exact=shop.id)
    transactions = Sales.objects.filter(shop_id__exact=shop.id)
    for prize in transactions:
        print(datetime.today().strftime("%d"))
    context = {
        'shop': shop,
        'prize_list': prize_list,
        'transactions': transactions
    }
    return render(request, 'index.html', context)
