# Generated by Django 4.2.3 on 2023-07-09 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0008_add_amount_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_amount',
            name='pincode',
        ),
    ]