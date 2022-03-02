from django.shortcuts import render
from django.http import HttpResponse
from jobs.models import Job
from jobs.models import Cities,JobTypes

# 职位列表
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context = {'job_list':job_list}

    return render(request,'joblist.html',context)

# 职位详情
def detail(request, job_id):
    job = Job.objects.get(id=job_id)

    return render(request,'job.html',{'job':job})

