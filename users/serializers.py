from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Used to return clean user details (excluding sensitive data like passwords)
    in API responses.
    """
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "is_vendor",
            "date_joined",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for User Registration.
    Handles validation of registration data and creation of a new user.
    """
    # write_only=True ensures these fields are accepted in the request
    # but never included in the response (security best practice).
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "password2",
        ]

    def validate(self, data):
        """
        Custom validation to ensure both password fields match.
        """
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data  # Fixed indentation: this must run if validation passes

    def create(self, validated_data):
        """
        Override the create method to handle password hashing.
        """
        # Remove password2 as it's not a field in the User model
        validated_data.pop("password2")

        # Use create_user() instead of create() to ensure the password is
        # hashed automatically by Django.
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for Login.
    This is a standard Serializer (not ModelSerializer) because it
    doesn't save data to the DB, it just validates the input credentials.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})


class UserWithTokenSerializer(serializers.ModelSerializer):
    """
    Serializer that wraps the User model and adds a custom 'token' field.
    Used to return user details + JWT token in one response after login/register.
    """
    # SerializerMethodField allows us to define a custom method (get_token)
    # to calculate the value of this field.
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "image", # Note: Ensure 'image' exists in your User model, or remove this.
            "is_vendor",
            "token",
        ]

    def get_token(self, obj):
        """
        Generates a JWT Refresh and Access token for the user.
        """
        refresh = RefreshToken.for_user(obj)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
    }
