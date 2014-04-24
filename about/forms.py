from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget = forms.TextInput(
            attrs = {'placeholder': 'Danny Milsom',
                     'class': 'form-control'})
        )
    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs = {'placeholder': 'dannymilsom@hotmail.co.uk',
                     'class': 'form-control'})
                 )
    message = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(
            attrs = {'placeholder': "Hi Danny, I'd like to talk about...",
                     'class': 'form-control', 'rows': 5})
                 )

    def __init__(self,  *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "contact-us-form"
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Get in touch', 
                                     css_id="contact-form-submit-btn",
                                     css_class="form-control"))
        self.helper.form_show_labels = False
        super(ContactForm, self).__init__(*args, **kwargs)