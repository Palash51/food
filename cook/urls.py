"""cook application URLs"""

from django.conf.urls import url, include


from . import views
from . import models

from cook.views import (
    CookListView,
    CookCreateView,
    CookDetailView,
    CookUpdateView,
    CookDeleteView,
)

urlpatterns = [
    url(r'^$', view=CookListView.as_view(), name='cook_list'),
    url(r'^create/$', view=CookCreateView.as_view(), name='cook_create'),
    url(r'^detail/(?P<pk>\d+)$', view=CookDetailView.as_view(), name='cook_detail'),
    url(r'^update/$', view=CookUpdateView.as_view(), name='cook_update'),
    url(r'^delete/$', view=CookDeleteView.as_view(), name='cook_delete'),
]
