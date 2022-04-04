from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin


# Create your models here.


class CustomUserManager(BaseUserManager):
    pass

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, username, password):
        return self._create_user(username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, verbose_name="Name", unique=True, blank=True)
    password = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=100, verbose_name="Email", unique=True)
    balance = models.IntegerField(verbose_name="Balance", default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Transaction(models.Model):
    amount = models.IntegerField(verbose_name='Amount')
    description = models.TextField(max_length=255, verbose_name="Description")
    datetime = models.DateTimeField(auto_now_add=True)
