from django.urls import path
from send_mail import views

app_name = 'send_mail'

urlpatterns = [
    path('', views.home, name='send_test'),
]