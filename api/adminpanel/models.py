from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name='', last_name='', phone_number='', password=None, **extra_fields):
        """ایجاد یک کاربر معمولی"""
        if not email:
            raise ValueError("ایمیل الزامی است")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """ایجاد سوپر یوزر"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("سوپر یوزر باید is_staff=True باشد.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("سوپر یوزر باید is_superuser=True باشد.")

        return self.create_user(username, email, password=password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    objects = CustomUserManager()  # مدیریت کاربر سفارشی

    def __str__(self):
        return self.username
