from django.db import models

from account_module.models import User


# Create your models here.

class HotelRoom(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    bed_room = models.SmallIntegerField(verbose_name='تعداد تخت')
    is_bb = models.BooleanField(default=False, verbose_name='همراه با صبحانه؟')
    price = models.IntegerField(verbose_name='قیمت')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = 'اتاق ها'


class DetailRoom(models.Model):
    title = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(verbose_name='عکس', upload_to='room/', null=True, blank=True)

    Reservation = models.BooleanField(verbose_name='رزرو شده/ نشده', null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = ' جزییات اتاق'
        verbose_name_plural = 'جزییات اتاق ها'


class Reserved(models.Model):
    room = models.ForeignKey(DetailRoom, related_name='hotel_booking', on_delete=models.CASCADE, verbose_name='اتاق')
    user = models.ForeignKey(User, related_name='user_booking', on_delete=models.CASCADE, verbose_name='شخص')
    date_in = models.DateField(verbose_name='تاریخ ورود', null=True)
    date_out = models.DateField(verbose_name='تاریخ خروج', null=True)

    def __str__(self):
        return str(self.room)

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو شده ها'

