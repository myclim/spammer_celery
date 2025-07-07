from django.contrib import admin
from celery_app.models import EmailUser



admin.site.register(EmailUser)