
from behave import given, when
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse


from account.models import OrderMeal


# @given('a user of the system and thali')
# def order_thali_food(context):
# 	""""""
# 	full_order = OrderMeal(name=self.order_meal.name,
# 										mobile="7299851985",
# 										email="palash@gmail.com",
# 										thali=self.order_meal.thali)

# 	# assert self.order_meal.name == "palash"

# @when('the user orders required number of thali')
# def submits_food_form(context):
# 	""""""
# 	