from django.shortcuts import render, redirect, get_object_or_404
from services.models import Service
from .models import Order
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from accounts.models import User


def home(request):
    return render(request, 'home.html')
@login_required
def create_order(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST' and request.user.role == 'client':
        Order.objects.create(
            client=request.user,
            service=service,
            status='pending'
        )
        return redirect('my_orders')
    return redirect('services_list')

@login_required
def my_orders(request):
    if request.user.role == 'client':
        orders = Order.objects.filter(client=request.user)
        return render(request, 'my_orders.html', {'orders': orders})
    return redirect('services_list')

from django.contrib.auth.decorators import user_passes_test

def is_worker(user):
    return user.is_authenticated and user.role == 'worker'

@user_passes_test(is_worker)
def worker_dashboard(request):
    orders = Order.objects.filter(worker=request.user)
    return render(request, 'worker_dashboard.html', {'orders': orders})

@user_passes_test(is_worker)
def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id, worker=request.user)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.progress_notes = request.POST.get('notes', '')
        order.save()
        return redirect('worker_dashboard')
    return render(request, 'update_order.html', {'order': order})

@role_required('client')
@login_required
def order_create(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        order = Order.objects.create(
            client=request.user,
            service=service,
            status='pending_review',  # ✅ корректно
            full_name=full_name,
            phone_number=phone_number,
            address=address
        )
        return redirect('order_detail', order.id)

    return render(request, 'order_create.html', {'service': service})



@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, client=request.user)
    return render(request, 'order_detail.html', {'order': order})


@role_required('worker')
@login_required
def worker_orders(request):
    orders = Order.objects.filter(worker=request.user).order_by('-created_at')
    return render(request, 'worker_orders.html', {'orders': orders})

@login_required
def worker_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, worker=request.user)

    if request.method == 'POST':
        status = request.POST.get('status')
        notes = request.POST.get('notes')
        if status in dict(Order.STATUS_CHOICES).keys():
            order.status = status
        order.notes = notes
        order.save()
        return redirect('worker_order_detail', order_id=order.id)

    return render(request, 'worker_order_detail.html', {'order': order, 'status_choices': Order.STATUS_CHOICES})


def no_access(request):
    return render(request, 'no_access.html')


import logging
logger = logging.getLogger(__name__)
@role_required('worker')
@login_required
def available_orders(request):
    orders = Order.objects.filter(worker__isnull=True, status='pending_review')
    logger.info(f"Доступные заказы для рабочего {request.user}: {orders}")
    return render(request, 'available_orders.html', {'orders': orders})


@role_required('worker')
@login_required
def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, worker__isnull=True, status='pending_review')

    if request.method == 'POST':
        order.worker = request.user
        order.status = 'in_progress'  # После принятия
        order.save()
        return redirect('worker_orders')

    return render(request, 'accept_order_confirm.html', {'order': order})