from datetime import datetime

from django.utils.timezone import make_aware
from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    context = {"name": "Пользователь"}
    return render(request, "hw/index.html", context)


from datetime import datetime
from django.utils.timezone import make_aware
from django.shortcuts import render
from . import models

def get_orders(request, user_id):
    current_datetime = datetime.now()

    orders = models.Order.objects.filter(customer=user_id)

    years_threshold = make_aware(current_datetime.replace(year=2022))
    months_threshold = make_aware(current_datetime.replace(month=3))
    weeks_threshold = make_aware(current_datetime.replace(day=current_datetime.day-7))

    this_years_orders = orders.filter(created_at__gt=years_threshold).distinct()
    this_months_orders = orders.filter(created_at__gt=months_threshold).distinct()
    this_weeks_orders = orders.filter(created_at__gt=weeks_threshold).distinct()


    this_years_items = models.Item.objects.filter(order__in=this_years_orders).distinct()

    context = {
        "year_data": this_years_orders,
        "month_data": this_months_orders,
        "week_data": this_weeks_orders,
        "year_items": this_years_items
    }

    return render(request, "hw/orders.html", context=context)


