"""cooks specific forms"""
from django import forms

from account.models import Position, BusinessUnit
from account.forms import BaseHorizontalForm

from .models import (
    Vacancy,
    Cook,
)


class CookCreateForm(BaseHorizontalForm):
    """Create cook form"""

    class Meta:
        """form meta class"""
        model = Cook
        fields = ['name', 'email', 'information']


class CookUpdateForm(BaseHorizontalForm):
    """Update cook form"""

    class Meta:
        """form meta class"""
        model = Cook
        fields = ['name', 'email', 'information']


class VacancyUpdateForm(BaseHorizontalForm):
    """Update vacancy form"""

    class Meta:
        """form meta class"""
        model = Vacancy
        fields = ['businessunit', 'position']



