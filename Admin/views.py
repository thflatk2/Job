from django.shortcuts import render
from django.views.generic.base import TemplateView
from Account.models import User
from Job.models import Job_info, Job_Apply
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


# Create your views here.

class AdminTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AdminTemplate, self).get_context_data(**kwargs)
        context['Applicant'] = User.objects.filter(type="Applicant")
        context['Employer'] = User.objects.filter(type="Employer")
        context['Jobs'] = Job_info.objects.all()
        context['Apply'] = Job_Apply.objects.all()
        context['Applicant_7'] = User.objects.filter(type="Applicant", date_joined__gte=datetime.now()-timedelta(days=7))
        context['Employer_7'] = User.objects.filter(type="Employer", date_joined__gte=datetime.now()-timedelta(days=7))
        context['Jobs_7'] = Job_info.objects.filter(created_date__gte=datetime.now()-timedelta(days=7))
        context['Apply_7'] = Job_Apply.objects.filter(created_date__gte=datetime.now()-timedelta(days=7))
        context['date'] = datetime.now()
        context['date_7'] = datetime.now()-timedelta(days=7)

        return context


class ApplicantTemplate(TemplateView):
    template_name = 'applicant_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantTemplate, self).get_context_data(**kwargs)
        context['Applicants'] = User.objects.filter(type="Applicant").order_by('-date_joined')

        return context

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        Appli_user = User.objects.filter(type="Applicant").order_by('-date_joined')
        paginator = Paginator(Appli_user, 10)  # Show 25 contacts per page

        try:
            Applicants = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Applicants = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            Applicants = paginator.page(paginator.num_pages)

        return render(request, 'applicant_admin.html', {'Applicants': Applicants})


class ApplicantDetailAdmin(TemplateView):
    template_name = 'applicant_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailAdmin, self).get_context_data(**kwargs)
        context['Applicant'] = User.objects.get(pk=self.kwargs['pk'])

        return context


class RecruiterTemplate(TemplateView):
    template_name = 'recruiter_admin.html'

    def get_context_data(self, **kwargs):
        context = super(RecruiterTemplate, self).get_context_data(**kwargs)
        context['Recruiters'] = User.objects.filter(type="Employer").order_by('-date_joined')

        return context

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        Emp_user = User.objects.filter(type="Employer").order_by('-date_joined')
        paginator = Paginator(Emp_user, 10)  # Show 25 contacts per page

        try:
            Recruiters = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Recruiters = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            Recruiters = paginator.page(paginator.num_pages)

        return render(request, 'recruiter_admin.html', {'Recruiters': Recruiters})


class RecruiterDetailTemplate(TemplateView):
    template_name = 'recruiter_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(RecruiterDetailTemplate, self).get_context_data(**kwargs)
        recruiter = User.objects.get(pk=self.kwargs['pk'])
        context['Recruiter'] = User.objects.get(pk=self.kwargs['pk'])
        context['Job'] = Job_info.objects.filter(user=recruiter.email)

        return context


class JobTemplate(TemplateView):
    template_name = 'job_admin.html'

    def get_context_data(self, **kwargs):
        context = super(JobTemplate, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.all().order_by('-created_date')

        return context

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        Job = Job_info.objects.all().order_by('-created_date')
        paginator = Paginator(Job, 10)  # Show 25 contacts per page

        try:
            Jobs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Jobs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            Jobs = paginator.page(paginator.num_pages)

        return render(request, 'job_admin.html', {'Jobs': Jobs})


class JobDetailAdmin(TemplateView):
    template_name = 'job_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailAdmin, self).get_context_data(**kwargs)
        context['Job'] = Job_info.objects.get(pk=self.kwargs['pk'])

        return context



class ApplyTemplate(TemplateView):
    template_name = 'apply_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ApplyTemplate, self).get_context_data(**kwargs)
        context['Applies'] = Job_Apply.objects.all().order_by('-created_date')

        return context

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        Apply = Job_Apply.objects.all().order_by('-created_date')
        paginator = Paginator(Apply, 10)  # Show 25 contacts per page

        try:
            Applies = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            Applies = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            Applies = paginator.page(paginator.num_pages)

        return render(request, 'apply_admin.html', {'Applies': Applies})


class ApplyDetailAdmin(TemplateView):
    template_name = 'apply_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ApplyDetailAdmin, self).get_context_data(**kwargs)
        context['Apply'] = Job_Apply.objects.get(pk=self.kwargs['pk'])

        return context
