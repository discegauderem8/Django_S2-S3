from django.db import models
from django.db.models import ManyToManyField



# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Товар {self.name} по цене {self.price}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = ManyToManyField(Item)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Заказ № {self.id} - {self.customer.name}. Заказ сделан {self.created_at} "
