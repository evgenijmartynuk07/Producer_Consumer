from django.urls import path

from orders.views import OrderListView, OrderDeleteView

urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path(
        "order/<int:pk>/delete/",
        OrderDeleteView.as_view(),
        name="order-delete"
    )

]

app_name = "orders"
