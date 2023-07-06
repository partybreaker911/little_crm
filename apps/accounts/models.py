from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from uuid import uuid4


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    phone_number = models.CharField(_("Phone Number"), max_length=14, blank=True, null=True)
    last_login = models.DateTimeField(_("Last Login"), blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.email}"

    @property
    def get_full_name(self) -> str:
        return self.first_name + " " + self.middle_name + " " + self.last_name
