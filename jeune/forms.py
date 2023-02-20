from django import forms
from jeune.models import subscribers, MailMessage


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = subscribers
        fields = ['email', ]

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'