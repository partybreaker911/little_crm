import secrets
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.accounts.tasks import send_registration_employee_email

"""
    TODO: 
        add class like BaseCustomUser that provide enheritance for CustomUser and Employee class
"""


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    first_name = models.CharField(_("First Name"), max_length=24)
    middle_name = models.CharField(_("Middle Name"), max_length=24)
    last_name = models.CharField(_("Last Name"), max_length=24)
    last_login = models.DateTimeField(_("Last login"), auto_now=True)

    def __str__(self):
        return self.email

    def employee_create(self, username, email, **kwargs):
        password = secrets.token_hex(16)
        employee = Employee(username=username, email=email, **kwargs)
        employee.set_password(password)
        employee.save()
        send_registration_employee_email(email, password)
        return employee

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Employee(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    first_name = models.CharField(_("First Name"), max_length=24)
    last_name = models.CharField(_("Last Name"), max_length=24)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="employee_groups",
        related_query_name="employee_group",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="employee_user_permissions",
        related_query_name="employee_user_permission",
    )

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")


class UserContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(_("Address"), max_length=150, blank=True, null=True)
    telephone = models.CharField(_("Telephone Number"), max_length=13, blank=True, null=True)

    class Meta:
        verbose_name = _("User Contacts")
        verbose_name_plural = _("User Contacts")

    def __str__(self):
        return f"{self.telephone}"


class BusinessProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="business_user")
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=12)

    class Meta:
        verbose_name = _("Business Profile")
        verbose_name_plural = _("Business Profiles")

    def __str__(self):
        return f"{self.user}"
