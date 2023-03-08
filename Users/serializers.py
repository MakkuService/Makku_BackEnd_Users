from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'Имя пользователя должно содержать только латинские симовлы и цифры'}

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('Логин должен содержать только латинские символы')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerialaizer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=70, min_length=6, write_only=True)
    username = serializers.CharField(max_length=70, min_length=6, read_only=True)
    tokens = serializers.CharField(max_length=70, min_length=6, read_only=True)

    class Meta:
        model=User
        fields=['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

 #       import pdb
 #       pdb.set_trace()
        if not user:
            raise AuthenticationFailed("Не совпадает логин или пароль, попоробуйте снова")

        if not user.is_active:
            raise AuthenticationFailed("Пользователь неактивен, обратитесь к администратору")

        if not user.is_verified:
            raise AuthenticationFailed("Email не подтвержден")

        return {
            'email':user.email,
            'username':user.username,
            'tokens': user.tokens()
        }

        return super().validate(attrs)

