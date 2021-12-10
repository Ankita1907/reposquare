from django.db import models
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from accounts.forms import (
    RegistrationForm,

)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from accounts.models import Profile





def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            num = request.POST['phone_number']
            emails=request.POST['email']
            passwrd = request.POST['password1']
            print(emails)
            print(passwrd)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(request.user)
            request.user.phone = num
            user1 = User.objects.get(username = request.user.username)
            profile = Profile.objects.get(user = user1)
            profile.phone =num
            profile.save()
            return redirect('/')
            
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/registration.html', args)


def login_here(request):
    message = 'Log In'
    if request.method == 'POST':
        
        _username = request.POST.get('email')
        _password = request.POST.get('pswd')
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                message = 'Not Activated'
        else:
            message = 'Invalid Login'
    context = {'message': message}
    return render(request, 'accounts/login.html', context)



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')