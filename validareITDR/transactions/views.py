from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import Product, Prize, Shop
from dashboard.views import get_active_campaign, get_selected_campaign, get_prize_list
from .models import Sales, ProductsSold
from django.http import JsonResponse
import json


@login_required
def transactions(request):
    context = {
        'product_list': get_campaign_products(),
        'active_campaign': get_active_campaign(),
        'selected_campaign': get_selected_campaign()
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
    quantity = int(request.GET.get('quantity'))
    if not quantity:
        return JsonResponse({'response': False})
    prize_list = get_prize_list(request)
    for prize in prize_list:
        if prize.min <= quantity <= prize.max:
            data = {
                'name': prize.name,
                'url_img': prize.url_img,
                'id': prize.id,
                'quantity': prize.quantity,
                'response': True
            }
    return JsonResponse(data)


@login_required
@csrf_exempt
def save_transaction(request):
    ticket_no = request.POST.get('ticketNo')
    products = json.loads(request.POST.get('productsSell'))
    prize_id = request.POST.get('idPrize')
    shop = Shop.objects.get(user__exact=request.user.id).id
    quantity = request.POST.get('quantity')
    campaign = get_selected_campaign()
    sale_id = save_sale(ticket_no, prize_id, shop, quantity, campaign)
    save_products_sold(products, sale_id)

    prize = get_prize(prize_id)
    prize.quantity = prize.quantity - 1
    prize.save()
    print(prize.quantity)

    return JsonResponse({'response': True})


def get_campaign_products():
    product_list = Product.objects.filter(promotional_campaign__exact=get_selected_campaign().id)
    return product_list


def save_sale(ticket_no, prize_id, shop, quantity, campaign):
    sales = Sales()
    sales.ticket_no = ticket_no
    sales.ticket_date = timezone.now()
    sales.prize_id = prize_id
    sales.shop_id = shop
    sales.total_sale = quantity
    sales.promotional_campaign = campaign
    sales.save()
    return sales.id


def get_prize(prize_id):
    prize = Prize.objects.get(id__exact=prize_id)
    return prize


def save_products_sold(products, sale_id):
    for product in products:
        product_sold = ProductsSold()
        product_sold.quantity = product['value']
        product_sold.product_id = product['id']
        product_sold.sale_id = sale_id
        product_sold.save()
