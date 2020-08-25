from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


class MyUserManager(BaseUserManager):
    def create_user(self, username, homepage, age, password=None):
        if not username:
            raise ValueError('Users must have username')
        user = self.model(
            username=username,
            homepage=homepage,
            age=age
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, age, password=None):
        user = self.create_user(
            username,
            password=password,
            age=age
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_display_name(self):
        return self.first_name + ' ' + self.last_name
