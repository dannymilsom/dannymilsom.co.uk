from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from about.forms import ContactForm


class AjaxableResponseMixin(object):
    """AJAX support for form submissions - to be used with a GCBV."""

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)

        form.send_mail()

        if self.request.is_ajax():
            thank_you_message = "Sent! Thanks for getting in touch {}.".format(
                form.cleaned_data['name'])
            data = {'message': thank_you_message }
            return JsonResponse(data)
        else:
            return response


class Homepage(AjaxableResponseMixin, FormView):
    """Returns the site homepage, with experience text and contact form."""

    form_class = ContactForm
    template_name = 'homepage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['gmail_address'] = settings.GMAIL_ADDRESS
        return context
