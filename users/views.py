# users/views.py

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserWithTokenSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         user = serializer.save()
         token_serializer = UserWithTokenSerializer(user)
         return Response(token_serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)

       user = authenticate( request, email=serializer.validated_data['email'], password=serializer.validated_data['password' )

       if not user:
          return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

          token_serializer = UserWithTokenSerializer(user)
      return Response(token_serializer.data, status=status.HTTP_200_OK)

                                                                                                                                                                        class ProfileView(generics.RetrieveAPIView):
                                                                                                                                                                            serializer_class = UserSerializer
                                                                                                                                                                                permission_classes = [permissions.IsAuthenticated]

                                                                                                                                                                                    def get_object(self):
                                                                                                                                                                                            return self.request.user