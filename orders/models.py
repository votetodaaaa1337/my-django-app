from django.db import models
from accounts.models import User
from services.models import Service

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending_review', 'На рассмотрении'),  # добавили
        ('in_progress', 'В процессе'),
        ('completed', 'Завершен'),
        ('rejected', 'Отклонён'),  # можно на будущее
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_orders')
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_orders')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    progress_notes = models.TextField(blank=True)

    full_name = models.CharField(max_length=100, default='Имя не указано')
    phone_number = models.CharField(max_length=20, default='Не указан')
    address = models.CharField(max_length=255, default='Не указан')
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} - {self.service.title}"



class ConstructionRequest(models.Model):
    BUILDING_TYPES = [
        ('house', 'Жилой дом'),
        ('garage', 'Гараж'),
        ('warehouse', 'Склад'),
        ('other', 'Другое'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='construction_requests')
    building_type = models.CharField(max_length=50, choices=BUILDING_TYPES)
    description = models.TextField()
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='pending_review')  # или 'ожидает рассмотрения'
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_constructions')

    def __str__(self):
        return f"Заявка на {self.get_building_type_display()} от {self.client.username}"


