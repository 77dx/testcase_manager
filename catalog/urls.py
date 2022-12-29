from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',RedirectView.as_view(url='/catalog/')),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)