from django.db import models


class AuthFields(models.Model):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, max_length=30)

    class Meta:
        abstract = True
