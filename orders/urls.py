from django.conf.urls import url
from . import views
from orders.views import (
    OrderHistory,
    ManageOrders
)

urlpatterns = [
    url(r'^create/$',
        views.order_create,
        name='order_create'),
    url(r'^myorders$', view=OrderHistory.as_view(), name='myorders'),
    url(r'^manage$', view=ManageOrders.as_view(), name='manage'),
    url(r'^accept_order$', view=ManageOrders.as_view(), name='accept_order'),
]
