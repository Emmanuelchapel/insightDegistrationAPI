from django.core.mail import send_mail
from django.conf import settings


def send_registration_email(registration):

    subject = "Registration Successful"

    message = f"""
Hello {registration.full_name},

Thank you for registering.

Your registration has been successfully completed.

Email: {registration.email}
Phone: {registration.phone_number}

We are happy to have you with us.

Thank you.
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[registration.email],
        fail_silently=False,
    )