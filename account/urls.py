from django.conf.urls import url
from django.conf import settings

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from account import views
from account.views import (
	RegisterUserView, 
	LoginUserView, 
	DashboardView, 
	OrderMealView, 
	OrderMealListView,
	LunchView 
	)

from django.contrib.auth.views import logout

urlpatterns = [
    # /account/register
    #url(r'^home/$', views.home, name='home'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    #url(r'^logout/$', auth_views.logout),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^orders/$', view=OrderMealView.as_view(), name='orders'),
    url(r'^dashboard/$', view=DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/myorders$', view=OrderMealListView.as_view(), name='myorders'),
    # url(r'^dashboard/myprofile$', view=Profile.as_view(), name='myprofile'),
    url(r'^lunch/$', view=LunchView.as_view(), name='lunch'),

    
]