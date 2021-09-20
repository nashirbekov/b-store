from rest_framework import serializers

from storeapp.models import Product, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "category", "name", "image", "description", "price")


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active",
                  "date_joined", "groups", "user_permissions")


class UsersIsActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active",
                  "date_joined", "groups", "user_permissions")
