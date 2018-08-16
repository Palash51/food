"""vacancy application django tables"""
import django_tables2 as tables

from django_tables2 import tables, TemplateColumn, Column
from django.utils.safestring import mark_safe
from django.template import Context, Template

from .models import (
    Vacancy,
    Cook,
)


class CookTable(tables.Table):
    """Table class for candidates"""
    Name = Column(
        verbose_name='Name',
        orderable=False,
        accessor='name')

    class Meta:
        """Meta class."""
        empty_text = 'No candidates to display'
        orderable = False
        model = Cook
        fields = (
            'name',
            'email',
            'information',
            'vacancy',
        )
        attrs = {"class": "table table-bordered table-hover"}

    actions = TemplateColumn(
        template_name="cook/tables/cook_actions.html",
        verbose_name='Actions',
    )

    name = TemplateColumn(
        template_name="cook/tables/cook_title.html",
        verbose_name='Name',
    )

