"""cook application views"""
from django.shortcuts import redirect, get_object_or_404
# from django.core.urlresolvers import reverse_lazy, reverse
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableView

from account.constants import ADD_COOK

from .models import (
    Vacancy,
    Cook,
)
from . import tables
from . import forms




class CookListView(LoginRequiredMixin, SingleTableView):
    """cook list"""
    template_name = 'cook/cook_list.html'
    model = Cook
    table_class = tables.CookTable
    context_object_name = 'cook'
    table_pagination = {"per_page": 15}

    # import pdb
    # pdb.set_trace()


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    """cook create"""
    template_name = 'cook/cook_create.html'
    model = Cook
    form_class = forms.CookCreateForm

    def get_queryset(self):
        queryset = Cook.objects.all()
        return queryset

    def get_success_url(self):
        """url to redirect to on success"""
        return reverse('cook:cook_list')


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    """cook update"""
    template_name = 'cook/cook_create.html'
    model = Cook
    form_class = forms.CookUpdateForm

    def get_success_url(self):
        """url to redirect to on success"""
        return reverse('cook:cook_list')


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    """cook details"""
    template_name = 'cook/cook_detail.html'
    model = Cook

    def get_success_url(self):
        """url to redirect to on success"""
        return reverse('cook:cook_list')


class CookDeleteView(LoginRequiredMixin, generic.View):
    """cook delete"""
    model = Cook

    def post(self, request, *args, **kwargs):
        """Delete a cook"""
        candidate_id = request.POST['remove']
        candidate = get_object_or_404(
            Candidate, pk=candidate_id)
        candidate.delete()
        return redirect(reverse('cook:cook_list'))

