from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class RegisterUser(generic.CreateView):
    """add a new user to NextHost"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register_user.html"
