from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=25)
    student_name = models.CharField(max_length=50)
    student_type = models.CharField(max_length=50)
    degree_id = models.CharField(max_length=20)
    degree_name = models.CharField(max_length=100)
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    degree_level_name = models.CharField(max_length=50)

class Degree_Level(models.Model):
    degree_level_name = models.CharField(max_length=50)
    degree_duration = models.CharField(max_length=10)

class Degree(models.Model):
    degree_id = models.CharField(max_length=20)
    degree_name = models.CharField(max_length=100)
    degree_level_name = models.CharField(max_length=50)
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    total_credit_hrs = models.CharField(max_length=10)

class Department(models.Model):
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    degree_id = models.CharField(max_length=20)
    degree_name = models.CharField(max_length=100)
    degree_level_name = models.CharField(max_length=50)

class Course(models.Model):
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    credit_hrs = models.CharField(max_length=10)
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    prereq_course_id = models.CharField(max_length=10, null=True)
    prereq_course_name = models.CharField(max_length=100, null=True)

class Transfer_Credit(models.Model):
    credit_hrs = models.CharField(max_length=10)