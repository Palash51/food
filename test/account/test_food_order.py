from datetime import timedelta, datetime, date
from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes import models as content_models


from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from account.models import OrderMeal

from test.account.helpers import FoodOrderTest


class FoodOrder(FoodOrderTest):
    """"""

    def test_order_meal_model(self):
        """"""
        full_order = OrderMeal(name=self.order_meal.name,
                               mobile="7299851985",
                               email="palash@gmail.com",
                               thali=self.order_meal.thali)
        assert self.order_meal.name == "palash"

    def test_get_user_login(self):
        """test get response of swift login"""
        self.client.login(username=self.user.username,
                          password=self.user.password)
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'account/login.html')

    def test_user_registration(self):
        """"""
        self.client.login(username=self.user.username,
                          password=self.user.password)
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'account/register.html')
