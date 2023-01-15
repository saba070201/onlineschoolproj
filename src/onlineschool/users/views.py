from django.shortcuts import render
def signup(request):
    return render(request,'users/signup.html')
def signin(request):
    return render(request,'users/signin.html')
# Create your views here.
