from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Income(TimeStampedModel):
    class Source(models.TextChoices):
        POCKET_MONEY = 'pocket_money', 'Pocket Money'
        SCHOLARSHIP = 'scholarship', 'Scholarship'
        FREELANCE = 'freelance', 'Freelance'
        OTHER = 'other', 'Other'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='incomes',
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=20, choices=Source.choices)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.amount} ({self.source})'