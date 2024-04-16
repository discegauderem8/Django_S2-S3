from django.urls import path
from .views import index, get_orders

urlpatterns = [
    path("", index, name="index"),
    path("orders/<int:user_id>/", get_orders, name="get_data"),
]
