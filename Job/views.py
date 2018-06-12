from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class JobListView(TemplateView):
    template_name = 'job_list.html'

class JobDetailView(TemplateView):
    template_name = 'job_detail.html'