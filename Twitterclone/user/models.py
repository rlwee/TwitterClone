from django.db import models
from django.contrib.auth.models import (
                                        BaseUserManager, 
                                        AbstractBaseUser,
                                        PermissionsMixin
                                        )

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('Must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_superuser=True
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address',
                              max_length = 50, 
                              unique=True
                             )

    objects = UserManager()
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

# Create your models here.
