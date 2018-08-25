from django.conf.urls import url, include
from django.contrib import admin
#from account.views import RegisterUserView, LoginUserView, DashboardView
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^account/',include("account.urls")),
    url(r'^cart/',include("cart.urls", namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^cook/', include('cook.urls', namespace='cook')),
    url(r'^notifications/', include('notify.urls', 'notifications')),
    url(r'^admin/', admin.site.urls),
]
