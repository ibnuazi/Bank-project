# Generated by Django 4.2.3 on 2023-07-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0004_bankmodel_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmodel',
            name='file',
            field=models.FileField(upload_to='bank_app/static'),
        ),
    ]
