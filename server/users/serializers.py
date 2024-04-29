from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

User = get_user_model()


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")
