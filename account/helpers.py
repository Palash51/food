from datetime import datetime, date, timedelta
from django.db.models import (Count, Sum, Case, When, Q, F, ExpressionWrapper, Aggregate, IntegerField)
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
	x = OrderItem.get_cost
	
	# total_amount_qu = OrderItem.objects.filter(customer=user).annotate(
 #    	total_weight=ExpressionWrapper(F('price') * F('quantity'), 
 #                                   output_field=IntegerField() ))
	total_amount = OrderItem.objects.filter(customer=user).aggregate(
        Sum('price'))['price__sum']

	return total_amount


