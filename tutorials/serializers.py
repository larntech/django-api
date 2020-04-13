from django.contrib.auth.models import User
from rest_framework import serializers, response, status


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login']
