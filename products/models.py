from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='laptops/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    review_book = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="review_book", null=True
    )
    stars = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_book} - {self.stars}"


class About(models.Model):
    about_us = models.TextField()

    def __str__(self):
        return self.about_us



