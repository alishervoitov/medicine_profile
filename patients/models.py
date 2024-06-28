from random import random

from django.contrib.auth.models import AbstractUser
from django.db import models

class Patient(AbstractUser):
    GENDER_CHOICE = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )
    Region = (
        ('Andijan', 'andijan'),
        ('Namangan', 'namangan'),
        ('Fergana', 'fergana'),
        ('Tashkent city', 'tashkent city'),
        ('Tashkent', 'tashkent'),
        ('Syrdayra', 'syrdarya'),
        ('Jizzakh', 'jizzakh'),
        ('Samarkand', 'samarkand'),
        ('Bukhara', 'bukhara'),
        ('Kharazem', 'kharazem'),
        ('Kashkadarya', 'kashkadarya'),
        ('Surhandarya', 'syrkhandarya'),
        ('Karakalpakstan', 'karakalpakstan'),
    )
    phone_number = models.CharField(
        max_length=50,
        unique=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICE)
    region = models.CharField(max_length=25, null=True, blank=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "email"]

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.phone_number


class Verification(models.Model):
    code = models.IntegerField(unique=True)
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)

    @classmethod
    def code_generate(cls, user):
        new_code = random.randint(10000,100000)
        while cls.objects.filter(code=new_code):
            new_code = random.randint(10000, 100000)
        obj = cls.objects.create(
            code=new_code,
            user=user
        )
        return obj