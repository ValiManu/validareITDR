from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import PromotionalCampaign, Shop, Prize
from transactions.models import Sales
from django.http import JsonResponse, HttpResponse


@login_required
def index(request):
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
