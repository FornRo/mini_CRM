from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Import User UpdateForm, ProfileUpdatForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from .models import Profile

__all__ = [
    'UserListView',
    'RegisterCreateView',
    'ProfileFormView',

    'profile',

    'password_reset_request',
]


class UserListView(generic.ListView):
    template_name = 'users/list.html'
    model = User
    paginate_by = 10


class RegisterCreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = r'Your account has been created! You are now able to log in'


class ProfileFormView(LoginRequiredMixin,
                      # SuccessMessageMixin,
                      generic.FormView):
    template_name = 'users/profile.html'
    form_class = UserUpdateForm
    work_form_class = ProfileUpdateForm
    success_message = f'Your account has been updated!'
    success_url = reverse_lazy('users:profile')

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST, instance=request.user)
        profile_form = self.work_form_class(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # return reverse_lazy(self.get_success_url())
            self.form_valid(self.get_form())
        # self.form_valid(u_form)

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if ('user_form' not in kwargs) and \
                ('profile_form' not in kwargs):
            user_form = UserUpdateForm(instance=self.request.user)
            profile_form = ProfileUpdateForm(instance=self.request.user.profile)
            kwargs['user_form'] = user_form
            kwargs['profile_form'] = profile_form
        return super().get_context_data(**kwargs)


# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')  # Redirect back to profile page

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)


# ____________________________________________


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})