# Generated by Django 4.1.5 on 2023-01-27 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0026_remove_detailroom_date_in_remove_detailroom_date_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserved',
            name='is_Reservation',
        ),
    ]