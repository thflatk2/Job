import json, os
from django.views.generic.base import TemplateView
from .forms import Job_InfoForm
from .models import Job_info, Job_Apply
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from Account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



# Create your views here.

class JobListView(TemplateView):
    template_name = 'job_list.html'

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

        return context

    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort', '')
        page = request.GET.get('page')
        Job = Job_info.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        paginator = Paginator(Job, 10)  # Show 25 contacts per page

        if sort == 'date_early':
            Job = Job_info.objects.all().order_by('start_date')
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'date_late':
            Job = Job_info.objects.all().order_by('-start_date')
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'period_long':
            Job = Job_info.objects.all().order_by('-contract_period')
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'period_short':
            Job = Job_info.objects.all().order_by('contract_period')
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'salary':
            Job = Job_info.objects.all().order_by('-min_salary')
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'kindergarten':
            Job = Job_info.objects.filter(Q(age_level__icontains='kindergarten'))
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'elementary':
            Job = Job_info.objects.filter(Q(age_level__icontains='elementary'))
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        elif sort == 'middle':
            Job = Job_info.objects.filter(Q(age_level__icontains='middle'))
            paginator = Paginator(Job, 10)
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            context = {'Jobs': Jobs}
            return render(request, 'job_list.html', context)
        else:
            try:
                Jobs = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Jobs = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Jobs = paginator.page(paginator.num_pages)

            return render(request, 'job_list.html', {'Jobs': Jobs})


class JobDetailView(TemplateView):
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.get(pk=self.kwargs['pk'])
        context['already'] = Job_Apply.objects.filter(job__pk=self.kwargs['pk']) & Job_Apply.objects.filter(user=self.request.user)

        return context

    def get(self, request, *args, **kwargs):
        boardData = Job_info.objects.get(id=self.kwargs['pk'])
        print(boardData.hits)
        Job_info.objects.filter(id=self.kwargs['pk']).update(hits=boardData.hits + 1)
        Jobs = Job_info.objects.get(pk=self.kwargs['pk'])
        already = Job_Apply.objects.filter(job__pk=self.kwargs['pk'])

        return render(request, 'job_detail.html', {'Jobs': Jobs, 'already': already})



'''
class JobUploadView(FormView):
    form_class = Job_InfoForm
    template_name = 'job_upload.html'
 
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print("asdasd")
        if form.is_valid():
            form = form.save()
            return redirect(form)
        else:
            form = Job_InfoForm()
            return render(request, 'job_list.html', {'form': form})
'''


def post_new(request):
    user_name = User.objects.get(name=request.user.name)

    if request.method == 'POST':
        form = Job_InfoForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid(): # form의 모든 validators 호출 유효성 검증 수행
            boardData = User.objects.get(slug=request.user.slug)
            User.objects.filter(slug=request.user.slug).update(job_count=boardData.job_count + 1)
            post = form.save() # PostForm 클래스에 정의된 save() 메소드 호출
            return redirect('Job:detail', post.id) # Model 클래스에 정의된 get_absolute_url() 메소드 호출
        else:
            form = Job_InfoForm()
            return render(request, 'job_upload.html', {'form': form, 'user_name':user_name})
    else:
        form = Job_InfoForm()
        return render(request, 'job_upload.html', {'form': form, 'user_name':user_name})


class JobApplyView(LoginRequiredMixin, CreateView):
    model = Job_Apply
    fields = ['profile_image1', 'profile_image2', 'last_name','first_name', 'email', 'country', 'gender', 'cur_residence', 'birth', 'graduate', 'estimate_graduate', 'university', 'major',
              'start_date', 'prefer_class', 'resume', 'job', 'user']
    template_name = 'job_apply.html'
    success_url = reverse_lazy('Job:list')

    def form_valid(self, form):
        boardData = Job_info.objects.get(id=self.kwargs['pk'])
        Job_info.objects.filter(id=self.kwargs['pk']).update(apply_count=boardData.apply_count + 1)

        return super(JobApplyView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(JobApplyView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.get(pk=self.kwargs['pk'])
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context


@login_required
@require_POST  # 해당 뷰는 POST method 만 받는다.
def job_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Job_info, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message,
               'nickname': request.user.profile.nickname}

    return HttpResponse(json.dumps(context), content_type="application/json")


class UserHistoryView(TemplateView):
    template_name = 'job_history.html'

    def get_context_data(self, **kwargs):
        context = super(UserHistoryView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_Apply.objects.filter(user=self.request.user).order_by('-created_date')
        context['Job_all'] = Job_info.objects.all()

        return context


class JobOverView(TemplateView):
    template_name = 'job_overview.html'

    def get_context_data(self, **kwargs):
        context = super(JobOverView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.filter(user=self.request.user.email)
        context['Job_all'] = Job_info.objects.all()
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context


class ApplicantListView(TemplateView):
    template_name = 'job_applicant_list.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantListView, self).get_context_data(**kwargs)
        context['applicant'] = Job_Apply.objects.filter(job__user=self.request.user.email)

        return context


class ApplicantDetailView(TemplateView):
    template_name = 'job_applicant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['applicant'] = Job_Apply.objects.get(pk=self.kwargs['pk'])

        return context


class ApplicantUpdateView(UpdateView):
    model = Job_Apply
    fields = ['profile_image1', 'profile_image2', 'last_name','first_name', 'email', 'country', 'gender', 'cur_residence', 'birth', 'graduate', 'estimate_graduate', 'university', 'major','start_date', 'prefer_class', 'resume']
    template_name = 'job_update_apply.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(ApplicantUpdateView, self).get_context_data(**kwargs)
        context['applicant'] = Job_Apply.objects.get(pk=self.kwargs['pk'])
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context


class JobUpdateView(UpdateView):
    model = Job_info
    fields = ['job_title', 'summary', 'school_name', 'class_size', 'start_date', 'age_level','location', 'contract_period', 'day_hour', 'min_salary', 'max_salary', 'flight_support', 'house', 'allowance','severance_payment', 'health_insurance', 'national_pension', 'house_pic1', 'house_pic2', 'house_pic3','house_pic4','house_pic5']
    template_name = 'job_upload_update.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['Job'] = Job_info.objects.get(pk=self.kwargs['pk'])

        return context


class JobDeleteView(DeleteView):
    model = Job_info
    template_name = 'job_delete.html'

    def get_context_data(self, **kwargs):
        context = super(JobDeleteView, self).get_context_data(**kwargs)
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        return reverse_lazy('Job:user_overview', kwargs={'slug': slug})