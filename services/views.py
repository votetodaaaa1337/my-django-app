from django.shortcuts import render
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

    category_labels = dict(Service.CATEGORY_CHOICES)

    services_by_category = []
    for key, label in category_labels.items():
        filtered_services = services.filter(category=key)
        if filtered_services.exists():
            services_by_category.append((label, filtered_services))

    context = {
        'services_by_category': services_by_category,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'services_list.html', context)

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})