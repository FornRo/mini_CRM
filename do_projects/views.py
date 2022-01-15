from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import DoProject

__all__ = [
    'ProjectListView',
    'ProjectDetailView',
    'ProjectCreateView',
    'ProjectUpdateView',
    'ProjectDeleteView',
]


class ProjectListView(PermissionRequiredMixin, generic.ListView):
    template_name = 'do_projects/list.html'
    model = DoProject
    paginate_by = 10
    permission_required = 'do_projects.view_doproject'


class ProjectDetailView(PermissionRequiredMixin,  generic.DetailView):
    template_name = 'do_projects/detail.html'
    model = DoProject
    permission_required = 'do_projects.view_doproject'


class ProjectCreateView(PermissionRequiredMixin, generic.CreateView):
    template_name = 'layouts/form.html'
    model = DoProject
    fields = '__all__'
    success_url = reverse_lazy('do_projects:list')
    permission_required = 'do_projects.add_doproject'


class ProjectUpdateView(PermissionRequiredMixin, generic.UpdateView):
    template_name = 'layouts/form.html'
    model = DoProject
    fields = '__all__'
    success_url = reverse_lazy('do_projects:list')
    permission_required = 'do_projects.change_doproject'


class ProjectDeleteView(PermissionRequiredMixin, generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = DoProject
    success_url = reverse_lazy('do_projects:list')
    permission_required = 'do_projects.delete_doproject'
