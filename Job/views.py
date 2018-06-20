import json, os
from django.views.generic.base import TemplateView
from .forms import Job_InfoForm
from .models import Job_info, Job_Apply
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from Account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class JobListView(TemplateView):
    template_name = 'job_list.html'

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

        return context


class JobDetailView(TemplateView):
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.get(pk=self.kwargs['pk'])

        return context

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
    if request.method == 'POST':
        form = Job_InfoForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
        if form.is_valid(): # form의 모든 validators 호출 유효성 검증 수행
            post = form.save() # PostForm 클래스에 정의된 save() 메소드 호출
            return redirect('Job:detail', post.id) # Model 클래스에 정의된 get_absolute_url() 메소드 호출
    else:
        form = Job_InfoForm()
        return render(request, 'job_upload.html', {'form': form, })


class JobApplyView(LoginRequiredMixin, CreateView):
    model = Job_Apply
    fields = ['profile_image1', 'profile_image2', 'last_name','first_name', 'email', 'skyid', 'country', 'gender', 'cur_residence', 'birth', 'degree',
              'start_date', 'prefer_class', 'resume', 'created_date', 'job', 'user', 'letter' ,'introduction']
    template_name = 'job_apply.html'
    success_url = reverse_lazy('Job:list')

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
        context['Jobs'] = Job_Apply.objects.filter(user= self.request.user)