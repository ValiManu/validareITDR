from django import forms


class Register(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)
    re_password = forms.CharField(max_length=30)

