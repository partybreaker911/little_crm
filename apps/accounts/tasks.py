from celery import shared_task

from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_registration_employee_email(email, password):
    context = {
        "password": password,
    }
    message = render_to_string("accounts/email/employee_registration_email.html", context)
    send_mail(
        "Welcome on site",
        message,
        "from@example.com",
        [email],
        fail_silently=False,
    )
