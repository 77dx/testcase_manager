from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=128,unique=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    status = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    token = models.CharField(max_length=256,blank=True,null=True,default=None)
    del_flag = models.DecimalField(max_digits=1, decimal_places=0,default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account

    class Meta:
        ordering = ['create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'