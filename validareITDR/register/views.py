from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import generate_token
from django.conf import settings
from django.core.mail import send_mail
from register.forms import Register
import re


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        email = form['email'].value().lower()
        username = form['username'].value().lower()
        first_name = form['first_name'].value()
        last_name = form['last_name'].value()
        password = form['password'].value()
        if form.is_valid():
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate your Account'
            message = render_to_string('activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            send_mail(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return redirect('login')
    return render(request, 'register.html')


def activate_account(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    user.is_active = True
    user.save()
    return redirect('login')


@csrf_exempt
def is_username(request):
    username = request.POST.get('username')
    if User.objects.filter(username__exact=username).exists():
        return JsonResponse({'data': True})
    return JsonResponse({'data': False})


@csrf_exempt
def is_email(request):
    email = request.POST.get('email')
    if User.objects.filter(email__exact=email).exists():
        return JsonResponse({'data': True})
    return JsonResponse({'data': False})


@csrf_exempt
def is_password(request):
    password = request.POST.get('password')
    reg = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$"
    pattern = re.compile(reg)
    if re.search(pattern, password):
        return JsonResponse({'data': False})
    return JsonResponse({'data': True})
