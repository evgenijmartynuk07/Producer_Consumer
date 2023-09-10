import datetime
import telebot

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from orders.models import Order
from producer_consumer.settings import API_TOKEN_TELEGRAM, CHAT_ID

bot = telebot.TeleBot(API_TOKEN_TELEGRAM)


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        context = super(OrderListView, self).get_context_data(**kwargs)

        return context

    def get_queryset(self) -> QuerySet:
        queryset = self.model.objects.select_related(
            "employee"
        ).filter(employee=self.request.user.id)

        return queryset


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("orders:order-list")

    @transaction.atomic
    def form_valid(self, form) -> HttpResponseRedirect:
        success_url = self.get_success_url()
        self.send_message_telegram()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def send_message_telegram(self) -> None:
        message = (
            f"Задача No{self.object.__str__()} під назвою {self.object.name} "
            f"була опрацьована {self.object.employee.__str__()}"
            f" у {datetime.datetime.now()}"
        )

        bot.send_message(chat_id=CHAT_ID, text=message)
