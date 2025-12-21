from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    Defines how users and superusers are created.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular User with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        
        # Normalize the email address (lowercase the domain part)
        email = self.normalize_email(email)
        
        # Create the user instance
        user = self.model(email=email, **extra_fields)
        
        # set_password hashes the password before saving it.
        # NEVER save a password directly without this method.
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a Superuser with the given email and password.
        """
        # Ensure superuser flags are set to True
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model.
    Inherits from AbstractBaseUser for full control over fields,
    and PermissionsMixin to handle permission/group logic automatically.
    """
    # Use email as the unique identifier instead of a username
    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    # is_active: Recommended to use this instead of deleting accounts (soft delete)
    is_active = models.BooleanField(default=True)
    
    # is_staff: Determines if the user can access the Django Admin site
    is_staff = models.BooleanField(default=False)
    
    # Custom field to distinguish vendors from regular customers
    is_vendor = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    
    image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        default="profile_images/default.jpg",
    )

    # Link the custom manager to this model
    objects = UserManager()

    # The field used for authentication (logging in)
    USERNAME_FIELD = "email"
    
    # Fields required when creating a user via the 'createsuperuser' command
    # (Password and USERNAME_FIELD are required by default)
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        # String representation of the user, usually the email
        return self.email
