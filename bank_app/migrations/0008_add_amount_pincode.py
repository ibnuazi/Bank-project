# Generated by Django 4.2.3 on 2023-07-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_add_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_amount',
            name='pincode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
