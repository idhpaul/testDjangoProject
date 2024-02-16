from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser

class BuyerManager( BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 테이블 이름 단수
# Attriubute snake_case
# Attribute lower case

class Buyer(AbstractBaseUser):

    email = models.CharField(unique=True, max_length=191)
    is_admin = models.BooleanField(default=False)
    # free_goods_count 무료 재화
    # pay_goods_count 유료 재화
    # device id

    objects = BuyerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
