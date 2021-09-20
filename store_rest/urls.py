from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='api_products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='api_product_detail'),
    path('users/', UsersListView.as_view(), name='api_users'),
    path('usersisactive/', UsersIsActiveListView.as_view(), name='api_users_is_active')
]
