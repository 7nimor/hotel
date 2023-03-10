# Generated by Django 4.1.5 on 2023-01-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('bed_room', models.SmallIntegerField(verbose_name='تعداد تخت')),
                ('is_bb', models.BooleanField(default=False, verbose_name='همراه با صبحانه؟')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('date_in', models.DateField(verbose_name='تاریخ ورود')),
                ('date_out', models.DateField(verbose_name='تاریخ خروج')),
            ],
        ),
        migrations.CreateModel(
            name='DetailRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('number', models.IntegerField(verbose_name='تعداد نفرات')),
                ('image', models.ImageField(null=True, upload_to='media/room', verbose_name='عکس')),
                ('Possibilities', models.CharField(choices=[('restoran', 'رستوران'), ('gem', 'باشگاه'), ('toilet', 'سرویس بهداشتی فرنگی'), ('service', 'سرویس روزانه اتاق'), ('Prayer ', 'نمازخانه')], max_length=200, verbose_name='امکانات')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.hotelroom', verbose_name='عنوان')),
            ],
        ),
    ]
