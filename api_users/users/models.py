from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Last Name', max_length=150, blank=True)
    other_name = models.CharField('Other Name', max_length=150, blank=True)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone')
    birthday = models.DateField(verbose_name='Birthday')
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        verbose_name='City',
        blank=True,
        null=True)
    additional_info = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Is Admin'
    )
    