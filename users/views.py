from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView

from . import forms, models, mixins


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = "auth/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    
# class UpdatePasswordView(
#     mixins.LoggedInOnlyView,
#     SuccessMessageMixin,
#     PasswordChangeView,
# ):

#     template_name = "users/update-password.html"
#     success_message = "Password Updated"

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#         form.fields["old_password"].widget.attrs = {"placeholder": "Current password"}
#         form.fields["new_password1"].widget.attrs = {"placeholder": "New password"}
#         form.fields["new_password2"].widget.attrs = {
#             "placeholder": "Confirm new password"
#         }
#         return form

#     def get_success_url(self):
#         return self.request.user.get_absolute_url()


# def log_out(request):
#     messages.info(request, f"See you later")
#     logout(request)
#     return redirect(reverse("core:home"))

