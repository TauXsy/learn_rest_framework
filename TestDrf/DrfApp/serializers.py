from .models import *
from rest_framework import serializers


class StudentModelSerializer(serializers.ModelSerializer):
    s_id = serializers.IntegerField(read_only=True)
    s_courses = serializers.SlugRelatedField(many=True, read_only=True, slug_field="course_name")
    s_cla_id = serializers.SlugRelatedField( read_only=True, slug_field="name")
    class Meta:
        model = Student
        fields = ['s_id','s_name','s_cla_id','s_courses']


class ClassModelSerializer(serializers.ModelSerializer):
    cla_id = serializers.IntegerField(read_only=True)
    cla_stus = serializers.SlugRelatedField(many=True, read_only=True, slug_field="s_name")
    class Meta:
        model = Class
        fields = ['cla_id','name','cla_stus']



class TeacherModelSerializer(serializers.ModelSerializer):
    t_id = serializers.IntegerField(read_only=True)
    t_course = serializers.SlugRelatedField( read_only=True, slug_field="course_name")
    class Meta:
        model = Teacher
        fields = ['t_id','name','t_course']


class CourseModelSerializer(serializers.ModelSerializer):
    c_id = serializers.IntegerField(read_only=True)
    c_stus = serializers.SlugRelatedField(many=True, read_only=True, slug_field="s_name")
    c_tea = serializers.SlugRelatedField( read_only=True, slug_field="name")
    class Meta:
        model = Course
        fields = ['c_id','course_name','c_stus','c_tea']

