from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address', 'comment']



class ConstructionRequestForm(forms.ModelForm):
    class Meta:
        model = ConstructionRequest
        fields = ['building_type', 'description', 'full_name', 'phone_number', 'address']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
