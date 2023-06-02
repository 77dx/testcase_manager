from django import forms
from django.core.exceptions import ValidationError
from . import models

class offerpriceForm(forms.Form):
    orderNo = forms.CharField(label="订单编号",error_messages={"required":"该字段不能为空"})
    phone = forms.CharField(label="手机号",error_messages={"required":"该字段不能为空"})

    def clean_orderNo(self):
        val = self.cleaned_data.get("orderNo")


    def clean_phone(self):
        val = self.cleaned_data.get("phone")
