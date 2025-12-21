from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserWithTokenSerializer,
    UserSerializer,
)
from django.contrib.auth import get_user_model

# Get the custom user model defined in the project settings
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user.
    It allows unauthenticated access and returns the user data with a token upon success.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user (guest) to access this endpoint

    def post(self, request, *args, **kwargs):
        # Validate the incoming data using the RegisterSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the new user instance
        user = serializer.save()

        # Serialize the user instance using the UserWithTokenSerializer
        # This ensures the response includes an authentication token for immediate login
        token_serializer = UserWithTokenSerializer(user)

        return Response(token_serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    """
    API view to authenticate a user.
    It validates credentials and returns the user profile along with an access token.
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Validate that email and password fields are present
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Use Django's built-in authentication system to verify credentials
        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        # If authentication fails, return a 401 Unauthorized response
        if not user:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        # If successful, serialize the user data with the token
        token_serializer = UserWithTokenSerializer(user)
        return Response(token_serializer.data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveAPIView):
    """
    API view to retrieve the currently logged-in user's profile.
    Requires the user to be authenticated.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only allow logged-in users

    def get_object(self):
        """
        Override the default get_object method.
        Instead of looking for a user by ID in the URL, return the user
        associated with the current request context.
        """
        return self.request.user
