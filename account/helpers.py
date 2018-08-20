from datetime import datetime, date, timedelta
from django.db.models import (Count, Sum, Case, When, Q)
from django.db.models.functions import Coalesce

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.models import User, Group

from account.models import UserProfile
from orders.models import OrderItem, Order
from shop.models import Category, Product
from cook.models import Cook


def get_total_calories(user):
    """"""
    calories = OrderItem.objects.filter(customer=user).aggregate(
        Sum('calories'))['calories__sum']
    return calories


def get_total_amount(user):
	""""""
	total_amount = OrderItem.objects.filter(customer=user).aggregate(
        Sum('price'))['price__sum']

	return total_amount

