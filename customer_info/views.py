from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import MultipleObjectMixin

from .models import Company
from .filters import *

__all__ = [
    'CompanyListView',
    'CompanyDetailView',
    'CompanyCreateView',
    'CompanyUpdateView',
    'CompanyDeleteView',
]


class CompanyListView(generic.ListView):
    template_name = 'customer_info/list.html'
    model = Company
    paginate_by = 10
    filter_class = CompanyFilter
    filter_obj = None

    def get_queryset(self):
        self.filter_obj = self.filter_class(self.request.GET, queryset=self.model.objects.all())
        return self.filter_obj.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter_obj
        return context


class CompanyDetailView(generic.DetailView):
    template_name = 'customer_info/detail.html'
    model = Company


class CompanyCreateView(generic.CreateView):
    template_name = 'layouts/form.html'
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')


class CompanyUpdateView(generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')


class CompanyDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Company
    success_url = reverse_lazy('customer_info:list')

