# Generated by Django 4.2.3 on 2023-07-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0010_withdraw_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ministatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stament', models.IntegerField(choices=[('withdraw', 'withdraw'), ('deposit', 'deposite')])),
            ],
        ),
    ]
