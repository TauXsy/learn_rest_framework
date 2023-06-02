from django.db import models

# Create your models here.
#老师 课程 一对一      学生 课程  多对多      班级 学生   一对多
class Student(models.Model):
    s_id = models.IntegerField(auto_created=True,primary_key=True,max_length=16)
    s_name = models.CharField(verbose_name='名字',max_length=32)

    s_cla_id = models.ForeignKey(to='Class',related_name='cla_stus', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.s_name

class Class(models.Model):
    cla_id = models.IntegerField(auto_created=True,primary_key=True,max_length=16)
    name = models.CharField(verbose_name='班级名称',max_length=32)

    def __str__(self):
        return self.name

class Course(models.Model):
    c_id = models.IntegerField(auto_created=True,primary_key=True,max_length=16)
    course_name = models.CharField(verbose_name='课程名称',max_length=255)

    c_stus = models.ManyToManyField(Student, related_name='s_courses')
    def __str__(self):
        return self.course_name

class Teacher(models.Model):
    t_id = models.IntegerField(auto_created=True,primary_key=True,max_length=16)
    name = models.CharField(verbose_name='名字',max_length=32)
    t_course = models.OneToOneField(Course, related_name='c_tea', on_delete=models.SET_NULL,  null=True)

    def __str__(self):
        return self.name


