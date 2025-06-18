from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('remont', 'Ремонт'),
        ('stroitelstvo', 'Строительство'),
        ('otdelka', 'Отделка'),
        ('demontazh', 'Демонтаж'),
        ('proektirovanie', 'Проектирование'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='stroitelstvo'
    )

    def __str__(self):
        return self.title

