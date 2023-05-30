from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = UserManager()


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)
