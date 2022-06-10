from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from api_users.constants import RESERVED_KEYWORD_ME
from users.models import User, UserRole


class UserAdminSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if 'username' in data:
            if data['username'] == RESERVED_KEYWORD_ME:
                raise serializers.ValidationError(
                    f'{RESERVED_KEYWORD_ME} - запрещенный username')
        return data

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(default=UserRole.USER)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class UserSignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        validators=[
            UnicodeUsernameValidator()
        ]

    )
    email = serializers.EmailField(
        max_length=254,
        validators=[
        ]
    )

    def validate(self, data):
        if 'username' in data and 'email' in data:
            if User.objects.filter(username=data['username']).exists():
                email = User.objects.get(username=data['username']).email
                if email != data['email']:
                    raise serializers.ValidationError(
                        'Неправильный email')
            if User.objects.filter(email=data['email']).exists():
                username = User.objects.get(email=data['email']).username
                if username != data['username']:
                    raise serializers.ValidationError(
                        'Неправильный username')
        return data

    def validate_username(self, value):
        if value == RESERVED_KEYWORD_ME:
            raise serializers.ValidationError(
                f'{RESERVED_KEYWORD_ME} - запрещенный username')
        return value


class UserGetTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.ReadOnlyField()
