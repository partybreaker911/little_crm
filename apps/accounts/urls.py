from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("employee/", views.EmployeeCreateView.as_view(), name="employee"),
]
