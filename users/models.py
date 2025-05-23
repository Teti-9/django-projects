from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUserModel(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_perms",
        blank=True,
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email