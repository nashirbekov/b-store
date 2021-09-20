from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Category(models.Model):
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name='subcategories',
                                        on_delete=models.CASCADE)
    name = models.CharField("Имя категории", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField("Имя продукта", max_length=255)
    image = models.ImageField("Изображение")
    description = models.TextField("Описание", null=True)
    price = models.DecimalField("Цена", max_digits=9, decimal_places=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
