# Generated by Django 4.2.3 on 2023-07-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0005_alter_bankmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankmodel',
            name='acc_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
