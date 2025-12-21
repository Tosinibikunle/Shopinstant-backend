from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """
    Custom Admin configuration for the custom User model.

    This class extends the default Django UserAdmin to support the custom
    User model (which likely uses email as the identifier instead of username)
    and includes custom fields like 'is_vendor'.
    """

    # Order the users in the list view by email address alphabetically
    ordering = ["email"]

    # Columns to display on the main "Select User" list page
    list_display = ["email", "first_name", "last_name", "is_vendor", "is_staff"]

    # Configuration for the "Edit User" page
    # This groups fields into collapsible sections
    fieldsets = (
        (None, {"fields": ("email", "password")}),  # Standard login info
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "phone_number")},
        ),  # Added 'phone_number' here
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_vendor",  # Added custom permission field
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined")},
        ),  # Standard tracking dates
    )

    # Configuration for the "Add User" page (initial creation form)
    # Replaces 'username' with 'email' since this is a custom email-based user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",  # Requires password set immediately
                    "password2",
                ),
            },
        ),
    )

    # Fields that can be searched via the search bar at the top of the list
    search_fields = ("email", "first_name", "last_name")


# Register the custom User model with the custom Admin configuration
admin.site.register(User, UserAdmin)
