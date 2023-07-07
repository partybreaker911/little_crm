from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from apps.accounts.models import UserContact

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_related_data(sender, instance, created, **kwargs):
    if created:
        UserContact.objects.create(user=instance)
