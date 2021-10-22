import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    uuid = models.UUIDField(
            unique=True,
            default=uuid.uuid4,
            editable=False,
            primary_key=False
            )
    role = models.CharField(max_length=10, verbose_name="Role of User")
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    uuid = models.UUIDField(
            unique=True,
            default=uuid.uuid4,
            editable=False,
            )
    description = models.TextField(verbose_name="Description")
    languages = ArrayField(models.CharField(max_length=25))
    country = models.CharField(max_length=20, verbose_name="Country")
    tags = ArrayField(models.CharField(max_length=15))
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, to_field='id')
    avatar = models.CharField(max_length=256, default='')

    def save(self, *args, **kwargs):
        if not self.avatar:
            if not self.user.first_name:
                Exception("First name and Last name is required")
            self.avatar = f"https://ui-avatars.com/api/?name={self.user.first_name}+{self.user.last_name}&background=0D8ABC&color=fff"
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} profile"
