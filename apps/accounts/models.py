from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


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

    def employee_create(self, username, password, **kwargs):
        employee = Employee(username=username, **kwargs)
        employee.set_password(password)
        employee.save()
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
