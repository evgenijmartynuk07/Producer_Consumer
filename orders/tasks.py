import random

from celery import shared_task
from .models import Order
from django.contrib.auth import get_user_model


@shared_task
def generated_new_order() -> None:
    users = get_user_model().objects.values_list("pk", flat=True)
    if users:
        user_id = random.choice(users)

        user = get_user_model().objects.get(pk=user_id)

        Order.objects.create(
            name="Тестовий запис",
            description="Тестовий запис для виконання",
            employee=user
        )
