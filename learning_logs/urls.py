"""Define padrões de URL para learning_logs."""
from django.urls import path
from . import views


name_app = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
]