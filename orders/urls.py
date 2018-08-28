from django.conf.urls import url
from . import views
from orders.views import (
    OrderHistory,
    ManageOrders,
    OrderDeleteView,
    OrderAcceptView,
    OrderDetailView,
)
from . import views

urlpatterns = [
    url(r'^create/$',
        views.order_create,
        name='order_create'),
    url(r'^myorders$', view=OrderHistory.as_view(), name='myorders'),
    url(r'^manage$', view=ManageOrders.as_view(), name='manage'),
    url(r'^remove$', view=OrderDeleteView.as_view(), name='remove'),
    # url(r'^accept_order$', view=ManageOrders.as_view(), name='accept_order'),
    url(r'^accept$', view=OrderAcceptView.as_view(), name='accept'),
    url(r'^detail/(?P<pk>\d+)$', view=OrderDetailView.as_view(), name='detail'),
]
