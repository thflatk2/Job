from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name='detail'),
    url(r'^upload/$', views.post_new, name='upload'),
    url(r'^like/$', views.job_like, name='job_like'),
    url(r'^(?P<pk>\d+)/add/$', views.JobApplyView.as_view(), name='apply'),
    url(r'^mypage/(?P<slug>[-\w]+)/history/$', views.UserHistoryView.as_view(), name='user_history'),
    url(r'^employer/(?P<slug>[-\w]+)/overview/$', views.JobOverView.as_view(), name='user_overview'),
    url(r'^employer/(?P<slug>[-\w]+)/applicants/$', views.ApplicantListView.as_view(), name='applicant_list'),
    url(r'^employer/(?P<slug>[-\w]+)/applicants/(?P<pk>\d+)/$', views.ApplicantDetailView.as_view(), name='applicant_detail'),
    url(r'^mypage/applicants/(?P<pk>\d+)/$', views.ApplicantUpdateView.as_view(), name='applicant_update'),
    url(r'^employer/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.JobUpdateView.as_view(), name='job_update'),
    url(r'^employer/(?P<slug>[-\w]+)/delete/(?P<pk>\d+)/$', views.JobDeleteView.as_view(), name='job_delete'),

]
