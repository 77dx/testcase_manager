from django.urls import path
from auto_test import views



urlpatterns = [
    path("api_userlist",views.api_userlist),
    path('api_login/',views.api_login),
]