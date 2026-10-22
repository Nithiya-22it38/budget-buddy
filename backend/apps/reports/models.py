from django.conf import settings
from django.db import models

from common.models import TimeStampedModel

FORMAT_CHOICES = [
    ('pdf', 'PDF'),
    ('excel', 'Excel'),
]


class Report(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    file_format = models.CharField(max_length=5, choices=FORMAT_CHOICES)
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return f'{self.month}/{self.year} ({self.file_format})'