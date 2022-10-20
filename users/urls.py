from . import views
from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns_user = [
    path('login/', LoginView.as_view(), {'template_name': 'users/login.html'}, name='login'),
    ]