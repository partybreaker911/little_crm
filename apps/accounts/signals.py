from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from apps.accounts.models import BusinessProfile

User = get_user_model()


# @receiver(post_save, sender=User)
# def create_user_related_data(sender, instance, create, **kwargs):
#     pass
