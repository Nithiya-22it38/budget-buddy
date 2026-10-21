from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=7, default='#6366F1')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='categories',
    )

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name