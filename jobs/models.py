from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳")
]
"""
职位类型，职位名称，工作地点，职位职责，岗位要求,创建人，创建日期，修改日期
"""
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,choices=JobTypes,verbose_name="职位类型")
    job_name = models.CharField(blank=False,max_length=250,verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False,choices=Cities,verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024,blank=False,verbose_name="职位职责")
    job_requirement = models.TextField(blank=False,max_length=1024,verbose_name="岗位要求")
    creator = models.ForeignKey(User,verbose_name="创建人",on_delete=models.SET_NULL,null=True)
    created_date = models.DateField(verbose_name="创建日期",default=datetime.now)
    modified_date = models.DateField(verbose_name="修改时间",default=datetime.now)
