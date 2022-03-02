from django.conf.urls import url
from django.urls import path
from jobs import views


urlpatterns = [
    path("joblist/", views.joblist, name="joblist"),
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail')
]