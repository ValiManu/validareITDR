from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import PromotionalCampaign, Shop, Prize, Network
from transactions.models import Sales
from django.http import JsonResponse
import pytz
import datetime


@login_required
def index(request):
    if not Shop.objects.filter(user__exact=request.user.id).exists():
        return render(request, 'user.html')
    context = {
        'shop': get_user_shop(request),
        'prize_list': get_prize_list(request),
        'transactions': get_transactions(request),
        'selected_campaign': get_selected_campaign(),
        'active_campaign': get_active_campaign()
    }
    return render(request, 'index.html', context)


@login_required
def change_campaign(request):
    context = {
        'campaigns': get_all_campaign(),
        'today_date': timezone.now(),
        'active_campaign': get_active_campaign(),
        'shop': get_user_shop(request)
    }
    return render(request, 'campaign.html', context)


def admin_configuration(request):
    return render(request, 'admin_configuration.html')


def campaign_configuration(request):
    return render(request, 'campaign_configuration.html')


def campaign_report(request):
    report = list(get_all_campaign().values())
    return JsonResponse(report, safe=False)


def campaigns_display(request):
    context = {
        'campaigns': get_all_campaign()
    }
    return render(request, 'campaign_configuration.html', context)


@csrf_exempt
def add_campaign(request):
    if request.method == 'POST':
        campaign_name = request.POST.get('campaignName')
        start_date = datetime.datetime.strptime(request.POST.get('startDate'), '%Y-%m-%dT%H:%M')
        timezone_ro = pytz.timezone('Europe/Bucharest')
        start_date = timezone_ro.localize(start_date)
        end_date = datetime.datetime.strptime(request.POST.get('endDate'), '%Y-%m-%dT%H:%M')
        end_date = timezone_ro.localize(end_date)
        network = request.POST.get('network')
        new_campaign = PromotionalCampaign(name=campaign_name, start_date=start_date, end_date=end_date)
        new_campaign.shops_network_id = network
        new_campaign.save()

    context = {
        'networks': Network.objects.all()
    }
    return render(request, 'add_campaign.html', context)


@csrf_exempt
def is_campaign_name(request):
    campaign_name = request.POST.get('campaignName').lower()
    if PromotionalCampaign.objects.filter(name__exact=campaign_name):
        return JsonResponse({'data': True})
    return JsonResponse({'data': False})


@csrf_exempt
def edit_campaign(request, pk):
    campaign = PromotionalCampaign.objects.get(id__exact=pk)
    if request.method == 'POST':
        campaign_name = request.POST.get('campaignName')
        start_date = datetime.datetime.strptime(request.POST.get('startDate'), '%Y-%m-%dT%H:%M')
        timezone_ro = pytz.timezone('Europe/Bucharest')
        start_date = timezone_ro.localize(start_date)
        end_date = datetime.datetime.strptime(request.POST.get('endDate'), '%Y-%m-%dT%H:%M')
        end_date = timezone_ro.localize(end_date)
        campaign.name = campaign_name
        campaign.start_date = start_date
        campaign.end_date = end_date
        campaign.save()
    context = {
        'campaign_name': campaign.name,
        'start_date': campaign.start_date.strftime("%Y-%m-%dT%H:%m"),
        'end_date': campaign.end_date.strftime("%Y-%m-%dT%H:%m"),
        'campaign_id': campaign.id
    }
    return render(request, 'edit_campaign.html', context)


@csrf_exempt
def set_campaigns(request):
    a = get_selected_campaign()
    a.selected_campaign = False
    a.save()
    selected_campaign = PromotionalCampaign.objects.get(id__exact=request.POST.get('activeCampaign'))
    selected_campaign.selected_campaign = True
    selected_campaign.save()
    return JsonResponse({'response': True})


def get_user_shop(request):
    shop = Shop.objects.get(user__exact=request.user.id)
    return shop


def get_prize_list(request):
    prize_list = Prize.objects.filter(shop_id__exact=get_user_shop(request).id,
                                      promotional_campaign_id__exact=get_selected_campaign().id)
    return prize_list


def get_selected_campaign():
    selected_campaign = PromotionalCampaign.objects.get(selected_campaign__exact=True)
    return selected_campaign


def get_transactions(request):
    transactions = Sales.objects.filter(shop_id__exact=get_user_shop(request).id,
                                        promotional_campaign_id__exact=get_selected_campaign().id)
    return transactions


def get_all_campaign():
    campaigns = PromotionalCampaign.objects.all()
    return campaigns


def get_active_campaign():
    if get_selected_campaign().end_date >= timezone.now():
        return True
    return False


@login_required
def sales_report(request):
    transactions = Sales.objects.filter(shop_id__exact=get_user_shop(request).id,
                                        promotional_campaign_id__exact=get_selected_campaign().id)
    list_transactions = []
    for transaction in transactions:
        data = {
            'campaign': PromotionalCampaign.objects.get(id__exact=transaction.promotional_campaign_id).name,
            'shop': Shop.objects.get(id__exact=transaction.shop_id).name,
            'ticket_no': transaction.ticket_no,
            'date': transaction.ticket_date,
            'total_sale': transaction.total_sale,
            'prize': Prize.objects.get(id__exact=transaction.prize_id).name
        }
        list_transactions.append(data)
    return JsonResponse(list_transactions, safe=False)


@login_required
def prize_list_report(request):
    awards = list(get_prize_list(request))
    prize_list = []
    for prize in awards:
        data = {
            'name': prize.name,
            'quantity': prize.quantity
        }
        prize_list.append(data)
    return JsonResponse(prize_list, safe=False)
