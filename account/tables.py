import calendar

from django_tables2 import tables, TemplateColumn, Column
from django.utils.safestring import mark_safe
from django.template import Context, Template

from .models import OrderMeal


class OrderMealTable(tables.Table):
    """table class to display the list of employee details"""
    Name = Column(
        verbose_name='Name',
        orderable=False,
        accessor='name'),
    mobile = Column(
        verbose_name='Contact No.',
        orderable=False,
        accessor='mobile')

    thali = Column(
        verbose_name='Thali',
        orderable=False,
        accessor='thali')

    delivery_date = Column(
        verbose_name='Date',
        orderable=False,
        accessor='delivery_date')

    class Meta:
        """Meta Attributes"""
        model = OrderMeal
        fields = (
            'name',
            'mobile',
            'thali',
            'delivery_date',
        )
        attrs = {"class": "table table-bordered"}
        per_page = 10
