from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
    ('student', 'Student'),
    ('premium', 'Premium User'),
    ('admin', 'Admin'),
]


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username