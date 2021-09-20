from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='base'),
    path('login/', BaseLoginView.as_view(), name='store_login'),
    path('register/', BaseRegisterView.as_view(), name='store_register'),
    path('logout/', BaseLogoutView.as_view(), name='store_logout'),
    path('profile/', profile, name='profile'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
