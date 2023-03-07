from django.contrib import admin
from django.urls import path
from users import views 
from django.urls import include, path


app_name='users'


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
]