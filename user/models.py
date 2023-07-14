from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .model.auth_fields import AuthFields
from .model.device_fields import DeviceFields
from .model.profile_fields import ProfileFields


class User(AbstractBaseUser, PermissionsMixin, AuthFields, DeviceFields, ProfileFields):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
