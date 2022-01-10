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


class ProjectListView(generic.ListView):
    template_name = 'do_projects/list.html'
    model = DoProject
    paginate_by = 10


class ProjectDetailView(generic.DetailView):
    template_name = 'do_projects/detail.html'
    model = DoProject


class ProjectCreateView(generic.CreateView):
    template_name = 'layouts/form.html'
    model = DoProject
    fields = '__all__'
    success_url = reverse_lazy('do_projects:list')


class ProjectUpdateView(generic.UpdateView):
    template_name = 'layouts/form.html'
    model = DoProject
    fields = '__all__'
    success_url = reverse_lazy('do_projects:list')


class ProjectDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = DoProject
    success_url = reverse_lazy('do_projects:list')
