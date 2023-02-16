from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Нужно присвоить Логин')
        if email is None:
            raise TypeError('Нужно указать Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return  user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Нужно указать Логин')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staf = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''


class auth_user_additional(models.Model):
    city = models.CharField(max_length=40, null=True, blank=True)
    coordinate = models.CharField(max_length=40, null=True, blank=True)
    IP = models.CharField(max_length=20, null=True, blank=True)
    lastpayment = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
