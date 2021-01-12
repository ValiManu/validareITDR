from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import Product, Prize, Shop
from dashboard.views import get_active_campaign, get_selected_campaign
from .models import Sales, ProductsSold
from django.http import JsonResponse
import json


@login_required
def transactions(request):
    context = {
        'product_list': get_campaign_products(),
        'active_campaign': get_active_campaign()
    }
    return render(request, 'transactions.html', context)


@login_required
def is_ticket_in_use(request):
    ticket = request.GET.get('ticket')
    result = 0
    if not ticket.isnumeric():
        result = 1
    elif ticket == '0':
        result = 1
    elif Sales.objects.filter(ticket_date__day=datetime.today().strftime("%d"),
                              shop_id__exact=get_object_or_404(Shop.objects.filter(user__exact=request.user.id)).id,
                              ticket_no__exact=ticket).exists():
        result = 2
    data = {
        'is_taken': result
    }
    return JsonResponse(data)


@login_required
def is_product_in_use(request):
    products = request.GET.getlist('products[]')
    check_products = 0
    data = {}
    for prod in products:
        check_products = check_products + int(prod)
    if check_products == 0:
        return JsonResponse({'response': False})
    else:
        prize_list = Prize.objects.all()
        for prize in prize_list:
            if prize.min < check_products <= prize.max:
                data = {
                    'name': prize.name,
                    'url_img': prize.url_img,
                    'id': prize.id,
                    'response': True
                }
    return JsonResponse(data)


@login_required
@csrf_exempt
def save_data(request):
    ticket_no = request.POST.get('ticketNo')
    products_sell = json.loads(request.POST.get('productsSell'))
    id_prize = request.POST.get('idPrize')
    shop = get_object_or_404(Shop.objects.filter(user__exact=request.user.id)).id
    product_list = Prize.objects.filter(shop__exact=shop)
    total_sold = 0
    for prod in products_sell:
        total_sold = total_sold + int(prod['value'])
    sales = Sales()
    sales.ticket_no = ticket_no
    sales.ticket_date = timezone.now()
    sales.prize_id = id_prize
    sales.shop_id = shop
    sales.total_sale = total_sold
    sales.save()
    for prod in products_sell:
        prod_sold = ProductsSold()
        prod_sold.quantity = prod['value']
        prod_sold.product_id = prod['id']
        prod_sold.sale_id = sales.id
        prod_sold.save()
    for prize in product_list:
        if prize.id == int(id_prize):
            prize.quantity = prize.quantity - 1
            prize.save()
    return JsonResponse({'response': True})


def get_campaign_products():
    product_list = Product.objects.filter(promotional_campaign__exact=get_selected_campaign().id)
    return product_list
