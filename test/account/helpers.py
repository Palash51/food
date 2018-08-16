from datetime import date, timedelta
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from account.models import OrderMeal

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class FoodOrderTest(TestCase):
	"""Base class for testing food order app"""

	def setUp(self):
		"""setup method for testing"""
		# import pdb
		# pdb.set_trace()
		self.user = User.objects.create(username='taha', password='1234', email='palash@gmail.com')
		self.order_meal = OrderMeal.objects.create(name="palash",
										thali=2)
