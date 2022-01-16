from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .filters import CooperationFilterSet
from .models import Cooperation

__all__ = [
    'CooperationListView',
    'CooperationDetailView',
    'CooperationCreateView',
    'CooperationUpdateView',
    'CooperationDeleteView',
    'CooperationByCompanyListView',
    'CooperationByProjectListView',
    'CooperationByUserListView',
]


class CooperationListView(PermissionRequiredMixin, generic.ListView):
    template_name = 'cooperation/list.html'
    model = Cooperation
    paginate_by = 10
    filterset_class = CooperationFilterSet
    filter_obj = None
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.view_cooperation'

    def get_queryset(self):
        self.filter_obj = self.filterset_class(self.request.GET, queryset=self.model.objects.all())
        return self.filter_obj.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter_obj
        return context


class CooperationByCompanyListView(PermissionRequiredMixin, generic.View):
    template_name = 'cooperation/list_filtered.html'
    model = Cooperation
    paginate_by = 10
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.view_cooperation'

    def get(self, rq, pk: int):
        object_list = Cooperation.objects.select_related('project').filter(project__company=pk)
        context = {
            'object_list': object_list,
            'page_obj': Paginator(object_list, self.paginate_by)
        }
        return render(rq, self.template_name, context=context)


class CooperationByProjectListView(PermissionRequiredMixin, generic.View):
    template_name = 'cooperation/list_filtered.html'
    model = Cooperation
    paginate_by = 10
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.view_cooperation'

    def get(self, rq, pk):
        object_list = self.model.objects.select_related('project').filter(project=pk)
        context = {
            'object_list': object_list,
            'page_obj': Paginator(object_list, self.paginate_by)
        }
        return render(rq, self.template_name, context=context)


class CooperationByUserListView(PermissionRequiredMixin, generic.View):
    template_name = 'cooperation/list_filtered.html'
    model = Cooperation
    paginate_by = 10
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.view_cooperation'

    def get(self, rq, pk):
        object_list = self.model.objects.select_related('project').filter(name_manager=pk)
        context = {
            'object_list': object_list,
            'page_obj': Paginator(object_list, self.paginate_by)
        }
        return render(rq, self.template_name, context=context)


class CooperationDetailView(PermissionRequiredMixin, generic.DetailView):
    template_name = 'cooperation/detail.html'
    model = Cooperation
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.view_cooperation'


# create update delete
class CooperationCreateView(PermissionRequiredMixin, generic.CreateView):
    template_name = 'layouts/form.html'
    model = Cooperation
    fields = '__all__'
    success_url = reverse_lazy('cooperation:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.add_cooperation'


class CooperationUpdateView(PermissionRequiredMixin, generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Cooperation
    fields = '__all__'
    success_url = reverse_lazy('cooperation:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.change_cooperation'


class CooperationDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Cooperation
    success_url = reverse_lazy('cooperation:list')
    login_url = reverse_lazy('profile:login')
    permission_required = 'cooperation.delete_cooperation'



