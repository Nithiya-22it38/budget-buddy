from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    college = models.CharField(max_length=150, blank=True)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='INR')
    budget_alert_percent = models.PositiveSmallIntegerField(default=80)
    email_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f'Profile of {self.user.username}'