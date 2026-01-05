# ModelSerializer is used to convert your model instances to JSON and vice versa.

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken

class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    seller = serializers.CharField(source="seller.username")

    class Meta:
        model = Product
        fields = [
            "public_product_id",
            "title",
            "price",
            "description",
            "image",
            "category",
            "seller",
            "created_at",
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        # Assign default role = user
        user_group = Group.objects.get(name="user")
        user.groups.add(user_group)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate

        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
            "role": user.groups.first().name if user.groups.exists() else "user"
        }
