# Generated by Django 5.0.2 on 2025-06-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('remont', 'Ремонт'), ('stroitelstvo', 'Строительство'), ('otdelka', 'Отделка'), ('demontazh', 'Демонтаж'), ('proektirovanie', 'Проектирование')], default='stroitelstvo', max_length=20),
        ),
    ]
