from django import forms


class TestClass(forms.Form):
    bill = forms.IntegerField(label="Numar Bon")

    def get_bon(self):
        bon = self.cleaned_data('bon_no')
        return bon
