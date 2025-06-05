from django.shortcuts import render
from django.db.models import Q
from services.models import Service

from django.db.models import Q
from services.models import Service

def services_list(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    services = Service.objects.all()

    if query:
        services = services.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if min_price:
        services = services.filter(price__gte=min_price)

    if max_price:
        services = services.filter(price__lte=max_price)

    context = {
        'services': services,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'services_list.html', context)

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})