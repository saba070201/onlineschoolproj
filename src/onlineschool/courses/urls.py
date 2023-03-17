from courses import views
from django.contrib import admin
from django.urls import path
from django.urls import include, path


app_name='courses'


urlpatterns=[
path('watch/',views.watch,name='watch'),

]
# будет watch/id видео 
# modules/ id курса
# будет 