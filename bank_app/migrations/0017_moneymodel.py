# Generated by Django 4.2.3 on 2023-08-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0016_wishlist_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='moneymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ac', models.IntegerField()),
                ('am', models.IntegerField()),
            ],
        ),
    ]
