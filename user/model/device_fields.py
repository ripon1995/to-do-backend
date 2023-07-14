from django.db import models


class DeviceFields(models.Model):
    device_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
