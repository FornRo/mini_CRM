from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Company
from .forms import CompanyForm


class CompanyListView(generic.ListView):
    template_name = 'customer_info/list.html'
    model = Company
    paginate_by = 10


class CompanyDetailView(generic.DetailView):
    template_name = 'customer_info/detail.html'
    model = Company


class CompanyCreateView(generic.CreateView):
    template_name = 'layouts/form.html'
    model = Company
    # form_class = CompanyForm
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')


class CompanyUpdateView(generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Company
    # form_class = CompanyForm
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')


class CompanyDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Company
    success_url = reverse_lazy('customer_info:list')

