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
]


class CooperationListView(generic.ListView):
    template_name = 'cooperation/list.html'
    model = Cooperation
    paginate_by = 10
    filter_class = CooperationFilterSet
    filter_obj = None


    def get_queryset(self):
        self.filter_obj = self.filter_class(self.request.GET, queryset=self.model.objects.all())
        return self.filter_obj.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter_obj
        return context


class CooperationByCompanyListView(generic.View):
    template_name = 'cooperation/list_company.html'
    model = Cooperation
    paginate_by = 10

    def get(self, rq, pk: int):
        object_list = Cooperation.objects.select_related('project').filter(project__company=pk)
        context = {
            'object_list': object_list,
            'page_obj': Paginator(object_list, self.paginate_by)
        }
        return render(rq, self.template_name, context=context)


class CooperationByProjectListView(generic.View):
    template_name = 'cooperation/list_project.html'
    model = Cooperation
    paginate_by = 10

    def get(self, rq, pk):
        object_list = self.model.objects.select_related('project').filter(project=pk)
        context = {
            'object_list': object_list,
            'page_obj': Paginator(object_list, self.paginate_by)
        }
        return render(rq, self.template_name, context=context)


class CooperationDetailView(generic.DetailView):
    template_name = 'cooperation/detail.html'
    model = Cooperation


# create update delete
class CooperationCreateView(generic.CreateView):
    template_name = 'layouts/form.html'
    model = Cooperation
    fields = '__all__'
    success_url = reverse_lazy('cooperation:list')


class CooperationUpdateView(generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Cooperation
    fields = '__all__'
    success_url = reverse_lazy('cooperation:list')


class CooperationDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Cooperation
    success_url = reverse_lazy('cooperation:list')



