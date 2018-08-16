"""cook models"""
from django.db.models import (
    SET_NULL,
    CASCADE,
    CharField,
    BooleanField,
    DateTimeField,
    ForeignKey,
    Model,
    EmailField,
    TextField,
)
from django.contrib.auth.models import User

from account.models import BusinessUnit, Position


class Vacancy(Model):
    """vacancy model"""
    businessunit = ForeignKey(
        BusinessUnit, related_name='vacancies', on_delete=CASCADE)
    position = ForeignKey(
        Position, related_name='vacancies', on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    is_open = BooleanField(default=True)

    def __str__(self):
        return '{} vacancy at {}'.format(
            self.position.name,
            self.businessunit.name
        )


class Cook(Model):
    """cook modele"""
    name = CharField(max_length=100, unique=True)
    email = EmailField(blank=False, null=False)
    information = TextField()

    def __str__(self):
        return self.name

