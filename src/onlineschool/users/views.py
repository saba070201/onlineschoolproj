from django.shortcuts import render
def signup(request):
    return render(request,'onlineschool/signup.html')
def signin(request):
    return render(request,'onlineschool/signin.html')
# Create your views here.
