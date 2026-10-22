from django.conf import settings
from django.db import models

from common.models import TimeStampedModel

SOURCE_CHOICES = [
    ('pocket_money', 'Pocket Money'),
    ('scholarship', 'Scholarship'),
    ('freelance', 'Freelance'),
    ('other', 'Other'),
]


class Income(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'