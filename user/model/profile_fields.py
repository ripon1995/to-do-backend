from django.db import models


class ProfileFields(models.Model):
    image_url = models.URLField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    full_name = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        abstract = True
