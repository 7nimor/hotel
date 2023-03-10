# Generated by Django 4.1.5 on 2023-01-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0004_alter_detailroom_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelroom',
            name='date_in',
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='date_out',
        ),
        migrations.AddField(
            model_name='detailroom',
            name='date_in',
            field=models.DateField(null=True, verbose_name='تاریخ ورود'),
        ),
        migrations.AddField(
            model_name='detailroom',
            name='date_out',
            field=models.DateField(null=True, verbose_name='تاریخ خروج'),
        ),
    ]
