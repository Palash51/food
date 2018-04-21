# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, FormView

from account.forms import RegisterUserForm, LoginForm, OrderMealForm
from .models import OrderMeal

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return render(self.request, 'account/welcome.html', {'form': form})
        #return HttpResponse('User registered')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

class OrderMealView(FormView):
    template_name = 'orders.html'
    form = OrderMealForm
    model = OrderMeal


    def post(self, request, *args, **kwargs):
        form = OrderMealForm(request.POST)
        
        if form.is_valid():
            order_meal = form.save()
            order_meal.name = request.POST['Name']
            order_meal.mobile = request.POST['number']
            order_meal.thali = request.POST['Thali']
            order_meal.message = request.POST['Message']
            order_meal.save()
            
        context= {'form': form }
        return render(request, 'index.html', )


 
