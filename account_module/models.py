from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    National_Id = models.CharField(max_length=10, verbose_name='کد ملی')
    phone_number = models.CharField(max_length=13, verbose_name='شماره تلفن')
    State = models.CharField(max_length=50, verbose_name='استان', null=True)
    city = models.CharField(max_length=50, verbose_name='شهر', null=True)

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.National_Id

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Staff(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    family = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    role = models.CharField(max_length=200, verbose_name='سمت')
    phone = models.CharField(max_length=200, verbose_name='شماره همراه', null=True, blank=True)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'کارکنان'
        verbose_name_plural = 'کارکنان'
