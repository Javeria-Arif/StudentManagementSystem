from django.contrib import admin
from django.contrib import admin
from .models import *
from django.contrib.admin.options import ModelAdmin

# Register your models here.

admin.site.register(Student)
admin.site.register(Section)
admin.site.register(TblClass)
admin.site.register(Course)
admin.site.register(schoolTeacher)
admin.site.register(Assignment)
admin.site.register(Day)
admin.site.register(TimeTable)
admin.site.register(SubmitAssignment)
admin.site.register(StudentResult)
admin.site.register(StudentAttendance)
admin.site.register(Tests)
admin.site.register(ContactForm)
admin.site.register(StudentComplaint)



