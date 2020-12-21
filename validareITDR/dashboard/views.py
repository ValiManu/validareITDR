from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Shop, Prize
from django.shortcuts import HttpResponse


@login_required
def index(request):
    shop = get_object_or_404(Shop.objects.filter(user__exact=request.user.id))
    product_list = Prize.objects.filter(shop__exact=shop.id)
    print('*' * 15)
    print(product_list)
    print('*' * 15)
    context = {
        'shop': shop,
        'product_list': product_list,
    }
    return render(request, 'index.html', context)
