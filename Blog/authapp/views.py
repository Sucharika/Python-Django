from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


from authapp.forms import PersonRegistrationForm, PersonLogin

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = PersonRegistrationForm
        return render(request,'register.html',{'form':form })
    else:
        form = PersonRegistrationForm(request.POST)
        if form.is_valid():
            fn= form.cleaned_data['first_name']
            ln=form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            uname= form.cleaned_data['username']
            pswd=form.cleaned_data['password']

            User.objects.create_user(first_name=fn,last_name=ln,email=email,username=uname,password=pswd)
            #send_mail(
                #'Account Created',
                #f'Yayyy, an account has been created with{uname}',
                #settings.EMAIL_HOST_USER,
                #[email,'018BIM057@sxc.edu.np'],
                #fail_silently=False,
            #)
            messages.success(request,'User created successfully')
            return redirect('Login')
        else:
            return render(request, 'register.html',{'form':form})

def sign_in(request):
    if request.method == 'GET':
        form=PersonLogin()
        return render(request,'login.html',{'form':form})
    else:
        next_url = request.GET.get('next')
        form = PersonLogin(request.POST)
        uname=request.POST['username']
        pswd=request.POST['password']
        user=authenticate(username=uname,password=pswd)
        if user is not None:
            login(request, user)
            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)
        else:
            messages.error(request,'Invalid Username or password')
            messages.error(request,'Please try again ')
            return render(request,'login.html',{'form':form})

def sign_out(request):
    logout(request)
    return redirect('Login')