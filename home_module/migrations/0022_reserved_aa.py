# Generated by Django 4.1.5 on 2023-01-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0021_remove_detailroom_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved',
            name='aa',
            field=models.ManyToManyField(db_index=True, null=True, to='home_module.detailroom'),
        ),
    ]
