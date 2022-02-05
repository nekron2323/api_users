from django.contrib.auth import get_user_model
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    other_name = models.CharField(
        max_length=200,
        verbose_name='Отчество',
        blank=True,
        null=True
    )
    email = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    birthday = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        verbose_name='Город')
    additional_info = models.TextField(
        verbose_name='Дополнительная информация'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Администратор'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name + self.last_name
