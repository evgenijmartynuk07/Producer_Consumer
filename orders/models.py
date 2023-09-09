import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    POSITION_CHOICES = [
        ("developer", "Розробник"),
        ("marketer", "Маркетолог"),
        ("salesperson", "Продавець"),
        ("manager", "Менеджер"),
    ]

    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    probation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}: {self.position}"


class Order(models.Model):
    task_id = models.CharField(
        max_length=7,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.task_id = self.generate_task_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_task_id():
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def __str__(self):
        return f"{self.pk}-{self.task_id}"
