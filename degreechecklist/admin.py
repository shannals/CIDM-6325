from django.contrib import admin
from .models import Student
from .models import Degree_Level
from .models import Degree
from .models import Course
from .models import Transfer_Credit
from .models import Department

admin.site.register(Transfer_Credit)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "student_name", "student_type", "degree_level_name", "dept_id", "dept_name", "degree_id", "degree_name")

admin.site.register(Student, StudentAdmin)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ("degree_id", "degree_name", "degree_level_name", "dept_id", "dept_name", "total_credit_hrs")

admin.site.register(Degree, DegreeAdmin)

class Degree_LevelAdmin(admin.ModelAdmin):
    list_display = ("degree_level_name", "degree_duration")

admin.site.register(Degree_Level, Degree_LevelAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "course_name", "credit_hrs", "dept_id", "dept_name", "prereq_course_id", "prereq_course_name")

admin.site.register(Course, CourseAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dept_id", "dept_name", "degree_id", "degree_name", "degree_level_name")

admin.site.register(Department, DepartmentAdmin)
