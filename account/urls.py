from django.conf.urls import url
from django.conf import settings

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views
from account import views
from account.views import (
	RegisterUserView, 
	LoginUserView, 
	DashboardView, 
	OrderMealView, 
	OrderMealListView,
	LunchView,
    UserProfileDetailView,
	)

from django.contrib.auth.views import logout

from django.urls import path


app_name = 'account'

urlpatterns = [
    # /account/register
    #url(r'^home/$', views.home, name='home'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    path('login/', view=LoginUserView.as_view(), name='login'),
    #url(r'^logout/$', auth_views.logout),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^orders/$', view=OrderMealView.as_view(), name='orders'),
    url(r'^dashboard/$', view=DashboardView.as_view(), name='dashboard'),
    # url(r'^dashboard/myorders$', view=OrderMealListView.as_view(), name='myorders'),
    url(r'^myprofile/(?P<pk>\d+)$', view=UserProfileDetailView.as_view(), name='myprofile'),
    # url(r'user/<int:pk>/', views=UserProfileDetailView.as_view(), name='user_detail'),
    url(r'^lunch/$', view=LunchView.as_view(), name='lunch'),


    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    
]