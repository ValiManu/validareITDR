from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Store, GroupStore, Campaign, Product
from django.shortcuts import HttpResponse


@login_required
def index(request):
    store = Store.objects.filter(allocate_user__exact='2')
    print('*' * 15)
    print(store)
    print('*' * 15)
    return render(request, 'index.html', context={'store': store})
