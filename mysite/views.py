#-*-coding:utf-8-*-
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from Account.forms import UserCreationForm,WebUserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from Account.models import User
from Job.models import Job_info
from django.shortcuts import  redirect



class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['Jobs'] = Job_info.objects.all().order_by('created_date')[:6]

        return context


class EmployerUpdateView(UpdateView):
    model = User
    fields = ['user_pic1', 'agency_name', 'cur_residence', 'name', 'phone', 'introduction']
    template_name = "employer.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(EmployerUpdateView, self).get_context_data(**kwargs)
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['user_pic1', 'user_pic2', 'first_name', 'last_name', 'country', 'gender', 'cur_residence', 'birth', 'graduate', 'estimate_graduate', 'university', 'major', 'resume']
    template_name = "mypage.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user_name'] = User.objects.get(name=self.request.user.name)

        return context


class LoginDoneView(TemplateView):
    template_name = "registration/login_done.html"


#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = WebUserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class WorkView(TemplateView):
    template_name = 'how_it_works.html'


class LifeView(TemplateView):
    template_name = 'life_in_korea.html'


class QualView(TemplateView):
    template_name = 'qualification.html'
