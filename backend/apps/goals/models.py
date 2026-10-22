from django.conf import settings
from django.db import models

from common.models import TimeStampedModel

STATUS_CHOICES = [
    ('active', 'Active'),
    ('completed', 'Completed'),
]


class SavingsGoal(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class GoalContribution(TimeStampedModel):
    goal = models.ForeignKey(SavingsGoal, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.goal.name} + {self.amount}'