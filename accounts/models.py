from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r"^[\w\s]+$",
        message="영어,숫자, _, 공백만 허용됩니다.",
        code="invalid_username",
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": "이미 사용중인 아이디입니다.",
        },
    )
    email = models.EmailField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    Role_CHOICES = [
        ("USER", "USER"),
        ("STAFF", "STAFF"),
        ("SUPERUSER", "SUPERUSER"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="roles"
    )
    role = models.CharField(
        max_length=10, choices=Role_CHOICES, blank=True, default="USER"
    )

    def __str__(self):
        return self.role
