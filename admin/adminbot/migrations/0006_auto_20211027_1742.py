# Generated by Django 3.1.13 on 2021-10-27 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminbot', '0005_auto_20211026_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='last_update_deposit_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 17, 42, 18, 247110), verbose_name='Последняя дата пополнения депозита'),
        ),
    ]
