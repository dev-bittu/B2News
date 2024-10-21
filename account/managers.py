from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for authentication
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email field must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Ensure password is not None
        if password:
            user.set_password(password)
        else:
            raise ValueError(_("The password field cannot be empty"))

        user.save(using=self._db)  # Save using the database
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_author", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        if extra_fields.get("is_author") is not True:
            raise ValueError(_("Superuser must have is_author=True."))

        return self.create_user(email, password, **extra_fields)
