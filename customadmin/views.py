from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from services.models import Service
from .forms import OrderForm, UserForm
from django.contrib.auth.decorators import user_passes_test


from accounts.models import User
from orders.models import Order

def is_admin(user):
    return user.is_authenticated and user.is_staff

from orders.models import Order

@user_passes_test(is_admin)
def dashboard(request):
    user = request.user
    context = {}

    if user.is_superuser:
        context['role'] = 'admin'
        context['orders'] = Order.objects.all().order_by('-created_at')  # передаем заказы в шаблон
    elif user.is_staff:
        context['role'] = 'manager'
    else:
        context['role'] = 'client'

    return render(request, 'admin_dashboard.html', context)


from orders.models import Order

def all_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'all_orders.html', {'orders': orders})

def all_users(request):
    users = User.objects.all().order_by('role')
    return render(request, 'all_users.html', {'users': users})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'edit_order.html', {'form': form})

@user_passes_test(is_admin)
def all_users(request):
    users = User.objects.all().order_by('role')
    return render(request, 'all_users.html', {'users': users})

@user_passes_test(is_admin)
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = UserForm()
    return render(request, 'edit_user.html', {'form': form})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_users')
    return render(request, 'delete_user.html', {'user': user})

def all_services(request):
    services = Service.objects.all()
    return render(request, 'all_services.html', {'services': services})

from decimal import Decimal, InvalidOperation

@user_passes_test(is_admin)
@user_passes_test(is_admin)
def add_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price_input = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category', 'repair')

        try:
            price = Decimal(price_input.replace(',', '.')) if price_input else Decimal('0')
        except (InvalidOperation, AttributeError):
            price = Decimal('0')

        if title:
            Service.objects.create(
                title=title,
                description=description,
                price=price,
                image=image,
                category=category,
            )
            return redirect('admin_services')
    return render(request, 'add_service.html', {'categories': Service.CATEGORY_CHOICES})



from decimal import Decimal, InvalidOperation
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_admin)
@user_passes_test(is_admin)
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.description = request.POST.get('description')
        price_input = request.POST.get('price')
        category = request.POST.get('category', 'repair')

        try:
            service.price = Decimal(price_input.replace(',', '.')) if price_input else Decimal('0')
        except (InvalidOperation, AttributeError):
            service.price = Decimal('0')

        if 'image' in request.FILES:
            service.image = request.FILES['image']

        service.category = category
        service.save()
        return redirect('admin_services')

    return render(request, 'edit_service.html', {'service': service, 'categories': Service.CATEGORY_CHOICES})



def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('admin_services')
    return render(request, 'delete_service.html', {'service': service})