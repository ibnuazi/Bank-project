# Generated by Django 4.2.3 on 2023-07-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0009_remove_add_amount_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdraw_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]