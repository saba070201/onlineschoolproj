from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method=='GET':
        return render(request,'users/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try: 
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                return redirect('home')
            except IntegrityError: 
                return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else: 
            return render(request, 'users/signup.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
 

def signin(request):
    if request.method=='GET':
        return render(request,'users/signin.html',{'form':AuthenticationForm()})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/signin.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')
        
        
@login_required
def signout(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
    
# Create your views here.
