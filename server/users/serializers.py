from djoser.serializers import UserSerializer

from .models import User


class JWTUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
        )
