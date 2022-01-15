from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Company
from .filters import *
from .forms import *

__all__ = [
    'CompanyListView',
    'CompanyDetailView',
    'CompanyCreateView',
    'CompanyUpdateView',
    'CompanyDeleteView',
]


class CompanyListView(PermissionRequiredMixin, generic.ListView):
    template_name = 'customer_info/list.html'
    model = Company
    paginate_by = 10
    filter_class = CompanyFilter
    filter_obj = None
    login_url = reverse_lazy('profile:login')
    permission_required = 'customer_info.view_company'

    def get_queryset(self):
        self.filter_obj = self.filter_class(self.request.GET, queryset=self.model.objects.all())
        return self.filter_obj.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter_obj
        return context


class CompanyDetailView(PermissionRequiredMixin, generic.DetailView):
    template_name = 'customer_info/detail.html'
    model = Company
    login_url = reverse_lazy('profile:login')
    permission_required = 'customer_info.view_company'


class CompanyCreateView(PermissionRequiredMixin, generic.CreateView):
    template_name = 'layouts/form.html'
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'customer_info.add_company'

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            kwargs['form_email'] = self.get_form(EmailForm)
            kwargs['form_phone'] = self.get_form(PhoneNumberForm)
        return super().get_context_data(**kwargs)


class CompanyUpdateView(PermissionRequiredMixin, generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('customer_info:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'customer_info.change_company'


class CompanyDeleteView(PermissionRequiredMixin, generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Company
    success_url = reverse_lazy('customer_info:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'customer_info.delete_company'

