from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ( "id", "email", "username", "password", )