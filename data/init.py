"""configuration imports, helpers and constants"""
import sys
import os

# Append project root directory to sys path
sys.path.append(os.getcwd())
# setup the environment
SETTINGS = 'base.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = SETTINGS

import django  # noqa
django.setup()

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission, Group


ADD_COOK = 'can_add_cooks'
ADD_FOOD_IN_CATEGORY = 'can_add_food_in_category'
COOK_REVIEW = 'can_review_cook'
FOOD_REVIEW = 'can_review_food'
RESTAURANT_REVIEW = 'can_review_restaurant'
ORDER_FOOD = 'can_order_food'


def add_user(username):
    user = User.objects.create_user(
        username=username, password=1234)
    return user


def add_group(group_name, permission_codes):
    user_ct = ContentType.objects.get_for_model(User)
    group, _ = Group.objects.get_or_create(name=group_name)

    permissions = []
    for code in permission_codes:
        permission, _ = Permission.objects.get_or_create(
            content_type=user_ct,
            codename=code,
            name=code.capitalize().replace('_', ' ')
        )

        permissions.append(permission)

    group.permissions.add(*permissions)


def add_user_to_group(username, group_name):
    user = User.objects.get(username=username)
    import pdb
    pdb.set_trace()
    group = Group.objects.get(name=group_name)
    user.groups.add(group)


def add_group_permissions_for_models(group_name, model_names):
    group = Group.objects.get(name=group_name)
    model_cts = ContentType.objects.filter(model__in=model_names)
    assert len(model_cts) > 0
    permissions = Permission.objects.filter(content_type__in=model_cts)
    assert len(permissions) > 0
    group.permissions.add(*permissions)
