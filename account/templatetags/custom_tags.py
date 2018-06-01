import calendar
import json
import math
from django import template
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from account.models import OrderMeal

register = template.Library()

@register.filter('orders_list')
def orders_list(all_orders):
	import pdb
	pdb.set_trace()
	return True