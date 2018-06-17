from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.JobDetailView.as_view(), name='detail'),
    url(r'^upload/$', views.post_new, name='upload'),
    url(r'^like/$', views.job_like, name='job_like'),
    url(r'^/(?P<pk>\d+)/add/$', views.JobApplyView.as_view(), name='apply')
]

