from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib import messages

from celery_app.forms import UserSaveForm, MessageForm
from celery_app.tasks import send_email_task
from celery_app.models import EmailUser




class MainView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Spammer'}
    

class SaveUserView(FormView):
    template_name = 'index.html'
    form_class = UserSaveForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Пользователь сохранен')
        return super().form_valid(form)


class MessageView(FormView):
    template_name = 'index.html'
    form_class = MessageForm
    success_url = '/'

    def form_valid(self, form):
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        user_emails = EmailUser.objects.only('email')

        for user in user_emails:
            send_email_task.delay(
                    subject=title,
                    message=text,
                    recipient_list=[user.email,],
                )
        messages.success(self.request, f"Задача отправки создана для {len(user_emails)} получателей")
        return super().form_valid(form)
