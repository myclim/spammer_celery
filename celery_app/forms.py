from django import forms
from celery_app.models import EmailUser




class UserSaveForm(forms.ModelForm):
    user = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = EmailUser
        fields = ['user', 'email']


class MessageForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

