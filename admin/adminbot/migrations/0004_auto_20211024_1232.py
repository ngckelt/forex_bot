# Generated by Django 3.1.8 on 2021-10-24 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminbot', '0003_auto_20211024_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='last_update_deposit_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 12, 32, 42, 751944), verbose_name='Последняя дата пополнения депозита'),
        ),
    ]