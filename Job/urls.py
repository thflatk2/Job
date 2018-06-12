from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.JobListView.as_view(), name='list'),
    url(r'^detail/$', views.JobDetailView.as_view(), name='detail'),

]

