# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django_tables2 import SingleTableMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect,  get_object_or_404
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.views.generic import CreateView, TemplateView, FormView, DetailView

from account.forms import RegisterUserForm, LoginForm, OrderMealForm
from .models import OrderMeal, UserProfile, Employee
from account import tables
from account.helpers import (
    get_total_calories,
    get_total_amount)


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"

    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        UserProfile.objects.create(user=User.objects.get(id=user.id))
        messages.success(
            self.request, "You have been successfully registered")

        return render(self.request, 'account/welcome.html', {'form': form})
        # return HttpResponse('User registered')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('account:dashboard')


@method_decorator(login_required, name='dispatch')
class DashboardView(SingleTableMixin, generic.ListView):
    """"""
    template_name = 'dashboard/dashboard.html'
    model = OrderMeal
    table_class = tables.OrderMealTable
    context_table_name = 'ordermeal_table'

    def get_context_data(self, **kwargs):
        context = super(DashboardView,
                        self).get_context_data(**kwargs)
        context['user_role'] = self.request.user.profile
        context['total_calories'] = get_total_calories(
            user=self.request.user.profile.username)
        context['total_amount'] = get_total_amount(
            user=self.request.user.profile.username)
        return context


class UserProfileDetailView(PermissionRequiredMixin, DetailView):
    """User profile details"""
    permission_required = []
    model = UserProfile
    template_name = 'dashboard/user.html'

    def get(self, request, *args, **kwargs):
        """returns user profile details"""
        user = get_object_or_404(
            UserProfile, user=self.kwargs['pk'])
        return render(
            request,
            'dashboard/user.html',
            {"user_data": user,
             'user_id': self.kwargs['pk']})


class OrderMealView(FormView):
    """meals order view"""
    template_name = 'index.html'
    form = OrderMealForm
    model = OrderMeal

    def post(self, request, *args, **kwargs):
        form = OrderMealForm(request.POST)

        if form.is_valid():
            order_meal = form.save()
            order_meal.name = request.POST['Name']
            order_meal.mobile = request.POST['number']
            order_meal.thali = request.POST['Thali']
            # order_meal.delivery_date = request.POST['datepicker2']
            order_meal.message = request.POST['Message']

            order_meal.save()

        context = {'form': form}
        return render(request, 'index.html', )


class OrderMealListView(SingleTableMixin, generic.ListView):
    """orders list views"""
    template_name = 'dashboard/table.html'
    model = OrderMeal
    table_class = tables.OrderMealTable
    context_table_name = 'ordermeal_table'

    def get_queryset(self):
        queryset = OrderMeal.objects.filter(name=self.request.user)
        return queryset


class LunchView(TemplateView):
    """lunch view for ordering lunch"""
    template_name = 'cart/cart.html'

