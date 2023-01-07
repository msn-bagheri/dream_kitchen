from django.db import models
from django.utils.translation import gettext_lazy as _

from app.choices import KitchenLayoutChoices


# Create your models here.


class UserForm(models.Model):
    layout = models.IntegerField(
        choices=KitchenLayoutChoices.choices,
        verbose_name=_('Kitchen Layout'),
        help_text=_('Kitchen Layout'),
    )
    a = models.CharField(
        max_length=255,
        verbose_name=_('A'),
        help_text=_('A'),
    )
    b = models.CharField(
        max_length=255,
        verbose_name=_('B'),
        help_text=_('B'),
        null=True,
        blank=True
    )
    c = models.CharField(
        max_length=255,
        verbose_name=_('C'),
        help_text=_('C'),
        null=True,
        blank=True
    )
    d = models.CharField(
        max_length=255,
        verbose_name=_('D'),
        help_text=_('D'),
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_('Email Address'),
        help_text=_('Email Address'),
    )
    budget = models.IntegerField(
        verbose_name=_('Budget'),
        help_text=_('Budget'),
    )
    current_kitchen = models.ImageField(
        verbose_name=_('Current Kitchen'),
        help_text=_('Current Kitchen'),
        upload_to='files/current_kitchens',
        null=True,
        blank=True,
    )
    desired_kitchen = models.ImageField(
        verbose_name=_('Desired Kitchen'),
        help_text=_('Desired Kitchen'),
        upload_to='files/desired_kitchens',
        null=True,
        blank=True,
    )
    is_island = models.BooleanField(
        verbose_name=_('Want Island'),
        help_text=_('Want Island'),
    )

    class Meta:
        ordering = ['id']
        verbose_name = _('User Form')
        verbose_name_plural = _('User Forms')

    def __str__(self):
        return "{} - {}".format(self.id, self.email)
