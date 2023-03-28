from django.db import models
class Course(models.Model):
    title=models.CharField(max_length=100,blank=True)
    memo=models.TextField(blank=True)
    hours=models.IntegerField(blank=True)
    price=models.IntegerField()
    def __str__(self):
        return str(self.title) + str(self.id)
    

class Module(models.Model):
    title=models.CharField(max_length=100,blank=True)
    memo=models.TextField(blank=True)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    number=models.IntegerField(blank=True)
    def __str__(self):
        return str(self.title) + str(self.id)
    

class Lesson(models.Model):
    title=models.CharField(max_length=100,blank=True)
    memo=models.TextField(blank=True)
    video=models.FileField(upload_to='courses/videos/')
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    number=models.IntegerField(blank=True)
    def __str__(self):
        return str(self.title) + str(self.id)
    

# class DownModule(models.Model):
#     title=models.CharField(max_length=100,blank=True)
#     memo=models.TextField(blank=True)
#     module_id=models.ForeignKey(Module,on_delete=models.CASCADE)
#     number=models.IntegerField(blank=True)

# class Videos(models.Model):
#     title=models.CharField(max_length=100,blank=True)
#     video=models.FileField(upload_to='courses/videos/')
# Create your models here.
