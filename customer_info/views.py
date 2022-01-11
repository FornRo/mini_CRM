from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.list import MultipleObjectMixin

from .models import Company
from .filters import CompanyFilter

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)

        filter_company = CompanyFilter(self.request.GET, queryset=self.get_queryset())
        paginated_filter_company = Paginator(filter_company.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        company_page_obj = paginated_filter_company.get_page(page_number)

        context['filter'] = filter_company
        context['object_list'] = company_page_obj
        context['page_obj'] = company_page_obj

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

