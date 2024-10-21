from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    avatar = models.ImageField(upload_to="avatar/", default="avatar/default.jpeg")

    is_author = models.BooleanField(default=False)
    author_website = models.URLField(default="https://github.com/dev-bittu/B2News.git")
    experience = models.CharField(max_length=200, default="Author | Programmer")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        # Normalize the email by converting it to lowercase
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
