from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from store_rest.serializers import ProductSerializer, ProductDetailSerializer, UsersSerializer, UsersIsActiveSerializer
from storeapp.models import Product, User


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersIsActiveListView(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UsersIsActiveSerializer
    permission_classes = [permissions.IsAuthenticated]
