# Generated by Django 4.1.5 on 2023-01-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0016_remove_hotelroom_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserved',
            options={'verbose_name': 'رزرو', 'verbose_name_plural': 'رزرو شده ها'},
        ),
        migrations.AddField(
            model_name='detailroom',
            name='Reservation',
            field=models.BooleanField(null=True, verbose_name='رزرو شده/ نشده'),
        ),
    ]
