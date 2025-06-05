from django import forms
from django.shortcuts import redirect, render
from orders.models import Order
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service', 'status', 'worker', 'full_name', 'phone_number', 'address']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'is_active']


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})