"""Define padrões de URL para learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatters = [
    path('', views.index, name='index'),
]