# Generated by Django 3.1.8 on 2021-10-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotAdmins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('telegram_id', models.CharField(max_length=255, verbose_name='ID в телеграмме')),
                ('active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Админ бота',
                'verbose_name_plural': 'Админы бота',
            },
        ),
        migrations.AlterField(
            model_name='clients',
            name='account',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Счет'),
        ),
    ]
