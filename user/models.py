from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .model.device_fields import DeviceFields
from .model.profile_fields import ProfileFields
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print("Super user created : ")
        print("Super user mail : " + email)
        print("Super user username : " + self.name)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(email=username)


class User(AbstractBaseUser, PermissionsMixin, DeviceFields, ProfileFields):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, max_length=128)

    is_staff = models.BooleanField(default=False)  # Include is_staff field
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
