from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("email"))
    username = models.CharField(max_length=150, unique=False, null=True, blank=True, verbose_name=_("username"))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    is_staff = models.BooleanField(default=True, verbose_name=_("is_staff"))
    is_superuser = models.BooleanField(default=True, verbose_name=_("is_superuser"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email