# Generated by Django 4.1.5 on 2023-01-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0014_alter_reserved_is_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='Reservation',
            field=models.BooleanField(null=True, verbose_name='رزرو شده/ نشده'),
        ),
    ]
