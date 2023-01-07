from django.db import models
from django.utils.translation import gettext_lazy as _


class KitchenLayoutChoices(models.IntegerChoices):
    SINGLE_WALL = 0, _('Single-Wall')
    GALLEY = 1, _('Galley')
    L_SHAPED = 2, _('L-Shaped')
    U_SHAPED = 3, _('U-Shaped')
    PENINSULA = 4, _('Peninsula')
    ISLAND = 5, _('Island')
