from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings




@shared_task(bind=True)
def send_email_task(self, subject, message, recipient_list):
    try:
        result = send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False
        )
        return result
    except Exception as err:
        print(f"Ошибка: {err}")
        raise
