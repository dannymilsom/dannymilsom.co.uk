from django import forms
from django.conf import settings
from django.core.mail import send_mail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):

    name = forms.CharField(
        label='Name',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Danny Milsom',
                'class': 'form-control col-xs-12'
            }
        )
    )
    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs = {
                'placeholder': settings.GMAIL_ADDRESS,
                'class': 'form-control col-xs-12'
            }
        )
    )
    message = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(
            attrs = {
                'placeholder': "Hi Danny, I'd like to talk about...",
                'class':'form-control col-xs-12',
                'rows': 4
            }
        )
    )

    def __init__(self,  *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "contact-us-form"
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit(
                'submit',
                'Get in touch',
                css_id="contact-form-submit-btn",
                css_class="form-control col-xs-12"
            )
        )
        self.helper.form_show_labels = False
        super(ContactForm, self).__init__(*args, **kwargs)

    def send_mail(self):
        """Send an email to the admin email address containing user message."""

        subject = 'Contact Form Submission'
        send_mail(
            subject,
            self.cleaned_data['message'],
            [self.cleaned_data['email']],
            [settings.GMAIL_ADDRESS]
        )
