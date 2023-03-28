from django.shortcuts import render,get_object_or_404
from .models import * 


def allcourses(request):
    courses=Course.objects.all()
    return render(request,'courses/allcourses.html',{'courses':courses})


def watchcourse(request,course_pk):
    course=get_object_or_404(Course,pk=course_pk)
    modules=Module.objects.filter(course_id=course_pk)
    return render(request,'courses/course.html',{'course':course,'modules':modules})


def watchlesson(request,course_pk,module_pk):
    lessons=Lesson.objects.filter(module_id=module_pk)
    return render(request,'courses/lesson.html',{'lessons':lessons})

def watch(request):
    return render(request,'courses/watch.html')
# Create your views here.
