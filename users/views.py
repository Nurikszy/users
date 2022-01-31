from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.views import generic

from users.forms import RegistrationForm, LoginForm


class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/users/'
    template_name = 'register.html'


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse("users:user_list")

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = "list.html"

    def get_queryset(self):
        return User.objects.all()
