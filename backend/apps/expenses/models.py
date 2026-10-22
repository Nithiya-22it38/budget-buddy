from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Expense(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'