from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=get_user_model())
def update_user_image_url(sender, instance, **kwargs):
    if instance.pk:
        original_user = sender.objects.get(pk=instance.pk)
        if original_user.image_url != instance.image_url:
            original_user.image_url = instance.image_url
            sender.objects.filter(pk=instance.pk).update(image_url=instance.image_url)

    else:
        instance.image_url = None
