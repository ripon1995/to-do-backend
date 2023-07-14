from django.db.models.signals import pre_save
from django.dispatch import receiver

from user.models import User


@receiver(pre_save, sender=User)
def update_user_image_url(sender, instance, **kwargs):
    if instance.pk:
        original_user = sender.objects.get(pk=instance.pk)
        if original_user.image_url != instance.image_url:
            original_user.image_url = instance.image_url
            sender.objects.filter(pk=instance.pk).update(image_url=instance.image_url)

    else:
        instance.image_url = None


@receiver(pre_save, sender=User)
def update_profile_full_name(sender, instance, **kwargs):
    if instance.pk:
        original_instance = sender.objects.get(pk=instance.pk)
        if original_instance.first_name != instance.first_name or original_instance.last_name != instance.last_name:
            instance.full_name = f"{instance.first_name} {instance.last_name}"
            sender.objects.filter(pk=instance.pk).update(full_name=instance.full_name)
    else:
        instance.full_name = None
