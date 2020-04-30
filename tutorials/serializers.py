from django.contrib.auth.models import User
from rest_framework import serializers, response, status


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user