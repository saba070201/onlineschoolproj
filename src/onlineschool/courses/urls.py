from courses import views
from django.contrib import admin
from django.urls import path
from django.urls import include, path


app_name='courses'


urlpatterns=[
path('watch/',views.watch,name='watch'),
path('allcourses/',views.allcourses,name='allcourses'),
path('course<int:course_pk>/',views.watchcourse,name='course'),
path('course<int:course_pk>/modules/module<int:module_pk>',views.watchlesson,name='watchlesson')

]
# будет watch/id видео 
# modules/ id курса
# будет 