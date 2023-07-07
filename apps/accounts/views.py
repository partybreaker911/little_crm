from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.accounts.models import Employee
from apps.accounts.services.profile import ProfileService

User = get_user_model()


class ProfileView(View, LoginRequiredMixin):
    template_name = "accounts/profile.html"

    def get(self, request):
        profile = ProfileService.get_user_info(user_id=self.request.user.id)
        context = {
            "profile": profile,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name)


class EmployeeCreateView(LoginRequiredMixin, View):
    template_name = "accounts/employee.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
