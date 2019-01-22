from django.db import models

from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    NullBooleanField)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from account.models import UserProfile
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=CASCADE,
    #                      related_name='user_customer')
    customer = models.CharField(max_length=100)
    product = models.ForeignKey(Product,
                                related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    calories = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=None)
    status = models.NullBooleanField(null=True, default=None)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_cost(self):
        return self.price * self.quantity
