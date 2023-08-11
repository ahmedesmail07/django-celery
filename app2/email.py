from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_email_review(name, email, review):
    context = {
        'name': name,
        'email': email,
        'review': review
    }
    email_subject = "Thanks for your review"
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_EMAIL_FROM, [email,],
    )
    return email.send(fail_silently=False)