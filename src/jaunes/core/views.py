from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from core.models import Business
from core.forms import BusinessForm


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['businesses'] = Business.objects.all()
        return ctx


class AddBusinessView(FormView):
    template_name = 'core/add_business.html'
    form_class = BusinessForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
