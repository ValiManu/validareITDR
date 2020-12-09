from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Store, GroupStore, Campaign, Product
from django.shortcuts import HttpResponse


@login_required
def index(request):
    store = get_object_or_404(Store.objects.filter(allocate_user__exact=request.user.id))
    product_list = Product.objects.filter(store__exact=store.id)
    print('*' * 15)
    print(product_list)
    print('*' * 15)
    context = {
        'store': store,
        'product_list': product_list,
    }
    return render(request, 'index.html', context)
