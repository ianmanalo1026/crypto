from django import forms
from .models import CryptoData


class CryptoDataForm(forms.ModelForm):
    class Meta:
        model = CryptoData
        fields = [
            'categories',
            'time_and_date',
            'prices',
        ]