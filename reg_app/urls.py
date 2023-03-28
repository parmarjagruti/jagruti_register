from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    #path('index/', index, name='index'),
    #path('ooty/', otp_fuction, name='otp_url'),
    path('ooty/', otp_function, name='otp_url'),
]