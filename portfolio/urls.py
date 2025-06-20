from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-message/', views.send_message, name='send_message'), # New URL pattern
]