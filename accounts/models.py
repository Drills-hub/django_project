from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    Role_CHOICES = [
        ("U", "USER"),
        ("S", "STAFF"),
        ("SU", "SUPERUSER"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="roles"
    )
    role = models.CharField(
        max_length=2, choices=Role_CHOICES, blank=True, default="U"
    )

    def __str__(self):
        return self.role
