# Generated by Django 4.2.5 on 2023-10-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0004_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
