# Generated by Django 3.1.8 on 2021-10-23 12:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminbot', '0004_clients_last_update_deposit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='last_update_deposit_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Последняя дата пополнения депозита'),
        ),
        migrations.CreateModel(
            name='Referrals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('telegram_id', models.CharField(max_length=255, verbose_name='ID в телеграмме')),
                ('username', models.CharField(blank=True, max_length=255, verbose_name='Юзернейм в телеграмме')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminbot.clients', verbose_name='Реферер')),
            ],
            options={
                'verbose_name': 'Реферал',
                'verbose_name_plural': 'Рефералы',
            },
        ),
    ]
