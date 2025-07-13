

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'is_vendor', 'date_joined']

    class RegisterSerializer(serializers.ModelSerializer):
         password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
         password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'password2']

    def validate(self, data):
       if data['password'] != data['password2']:
           raise serializers.ValidationError("Passwords do not match.")
           return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
      email = serializers.EmailField()    
      password = serializers.CharField(write_only=True, style={'input_type': 'password'})

class UserWithTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'is_vendor', 'token']

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }