from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True, db_index=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    profile_photo = models.FileField(null=True, upload_to='media/profile_photos')
    resume = models.FileField(null=True, upload_to='media/resumes')

    phone = models.CharField(max_length=12, null=True, blank=True)
    phone_confirmed = models.BooleanField(default=False)

    last_login = models.DateTimeField(null=True)
    last_login_ip = models.GenericIPAddressField(null=True)
