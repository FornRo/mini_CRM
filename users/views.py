from django.urls import reverse_lazy
from django.views import generic

from .models import Profile

__all__ = [
    'UserListView',
    'UserCreateView',
    'UserUpdateView',
    'UserDeleteView',
]


class UserListView(generic.ListView):
    template_name = 'users/list.html'
    model = Profile
    paginate_by = 10


class UserCreateView(generic.CreateView):
    template_name = 'layouts/form.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('user:list')


class UserUpdateView(generic.UpdateView):
    template_name = 'layouts/form.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('user:list')


class UserDeleteView(generic.DeleteView):
    template_name = 'layouts/confirm_delete.html'
    model = Profile
    success_url = reverse_lazy('user:list')
