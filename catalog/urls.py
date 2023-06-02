from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('offerprice',views.offerprice)
]