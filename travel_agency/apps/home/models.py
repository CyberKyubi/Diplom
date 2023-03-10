from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from slugify import slugify


class Countries(models.Model):
    class ManufacturingCountry(models.TextChoices):
        ITALY = 'IT', _('Италия')
        SWITZERLAND = 'CH', _('Швейцария')
        FRANCE = 'FR', _('Франция')
        IRELAND = 'IE', _('Ирландия')
        JAPAN = 'JP', _('Япония')
        NORWAY = 'NO', _('Норвегия')

    country = models.CharField(
        verbose_name='Страна',
        max_length=2,
        choices=ManufacturingCountry.choices,
    )
    country_image = models.ImageField(upload_to='img/products/', verbose_name='Каталог')

    def __str__(self):
        return self.get_country_display()

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(
        verbose_name='По какой стране путешествовал(а)',
        max_length=2,
        choices=Countries.ManufacturingCountry.choices,
    )
    rating = models.IntegerField(
        verbose_name='Оценка от 1 до 5',
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    text = models.CharField(max_length=1024, verbose_name='Отзыв')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.user.username, self.user.last_name)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'