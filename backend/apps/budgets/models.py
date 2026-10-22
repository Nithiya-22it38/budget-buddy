from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Budget(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.username} - {self.month}/{self.year}'