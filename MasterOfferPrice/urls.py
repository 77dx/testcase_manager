from django.urls import path
from . import views



urlpatterns = [
    path("offerprice/",views.offerprice)
]