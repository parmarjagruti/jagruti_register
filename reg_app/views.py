from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from random import randrange

# Create your views here.

def register(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        try :
            u_obj = User.objects.get(email = request.POST['email'])
            return render(request, 'register.html',{'msg':'Email Is Already register !!'})
        except :
            if request.POST['password'] == request.POST['repassword']:
                global c_otp,f
                f = [request.POST['full_name']]
                e = [request.POST['email']]
                p = [request.POST['password']]
                c_otp = randrange(1000000,999999, -1)
                send_mail(
                    'Welcome',
                    f'your OTP is 1234{c_otp}',
                    settings.EMAIL_HOST_USER,
                    [request.POST['email']])
                return render(request, 'otp.html',)
            else :
                return render(request,'register.html', {'msg': 'Both Password do not match !!'})
            


def otp_function(request):
    if str(c_otp) == request.POST['ooty']:
        User.objects.create(
            full_name = f,
            email = e,
            password = p
        )
        return render(request,'register.html', {'msg':'Successfully Register !!'})
    else:
        return render(request, 'otp.html', {'k' : 'wrong OTP'})