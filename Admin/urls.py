from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AdminTemplate.as_view(), name='home'),
    url(r'^applicants/$', views.ApplicantTemplate.as_view(), name='applicant_admin'),
    url(r'^applicants/detail/(?P<pk>\d+)/$', views.ApplicantDetailAdmin.as_view(), name='applicant_detail_admin'),
    url(r'^recruiters/$', views.RecruiterTemplate.as_view(), name='recruiter_admin'),
    url(r'^recruiters/detail/(?P<pk>\d+)/$', views.RecruiterDetailTemplate.as_view(), name='recruiter_detail_admin'),
    url(r'^job/$', views.JobTemplate.as_view(), name='job_admin'),
    url(r'^job/detail/(?P<pk>\d+)/$', views.JobDetailAdmin.as_view(), name='job_detail_admin'),
    url(r'^apply/$', views.ApplyTemplate.as_view(), name='apply_admin'),
    url(r'^apply/detail/(?P<pk>\d+)/$', views.ApplyDetailAdmin.as_view(), name='apply_detail_admin'),

]