from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import DateField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.db.models.query_utils import select_related_descend
from django.utils import tree
from django.contrib.auth.models import User

# Create your models here.


class TblClass(models.Model):
    classid = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50,null= True)
    class_code = models.CharField(max_length=50,null= True)
    
    def __str__(self):
        return self.class_code

class Section(models.Model):
    sectionid = models.AutoField(primary_key=True)
    sectionname = models.CharField(max_length=500,null= True)
    classid = models.ForeignKey(TblClass,null= True,on_delete=models.SET_NULL)
    
    
    def __str__(self):   
        return self.sectionname


class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursedescription = models.CharField(max_length=500,null= True)
    coursename = models.CharField(max_length=50,null= True)
#    userid = models.ForeignKey(Client,null= True,on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=50,null= True)
#    videolink = models.CharField(max_length=500 ,null= True)
#    roleid = models.ForeignKey(RoleName,null=True,on_delete=models.DO_NOTHING)
#    createddate = models.DateTimeField()
 #   imagelink = models.CharField(max_length='')
 #   duration = models.DateTimeField()
#    longdes = models.CharField(max_length='')
 #   coursetype = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass,null=True,on_delete=models.DO_NOTHING)
 #   assignto = models.CharField(max_length='')
 #   status = models.BinaryField(null = True)
 
    def __str__(self):
        return self.coursename

class schoolTeacher(models.Model):
    teacherid = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=200, null=True)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    t_img = models.ImageField(default="download.png", null = True,blank = True)
    regno = models.CharField(max_length=20)
    joiningdate = models.DateTimeField()
    courseid = models.ForeignKey(Course, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.t_name


class Day(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null =True)
    
    
    def __str__(self):
        return self.name


    
    
class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    tt_name = models.CharField(max_length=200,null= True)
    classid = models.ForeignKey(TblClass,null=True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    sectionid = models.ForeignKey(Section,null=True,on_delete=models.DO_NOTHING)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
  #  allocationstatus = models.CharField(max_length=100,null=True)
    dayid = models.ForeignKey(Day,null=True,on_delete=models.DO_NOTHING)
    
  



class Student(models.Model):
    user = models.OneToOneField(User,null =True,on_delete=models.CASCADE)
    
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    regno = models.CharField(max_length=20,null=True)
    registrationdate = models.DateTimeField(null =True)
    address = models.CharField(max_length=100,null =True)
    classid = models.ForeignKey(TblClass,null=True, on_delete=models.SET_NULL)
   # schoolid = models.ForeignKey(School,null=True, on_delete=models.SET_NULL)
    sectionid = models.ForeignKey(Section,null=True, on_delete=models.SET_NULL)
    std_profile = models.ImageField(default="download.png", null = True,blank = True)

    
    def __str__(self):
        return self.sname
    
class Assignment(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    assignmentname = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment = models.FileField(max_length=500, default='no assignment yet',upload_to='images')
    duedate = models.DateTimeField()
    createddate = models.DateTimeField()
    teacherid = models.ForeignKey(schoolTeacher, on_delete=models.CASCADE, default= 0)

    def __str__(self):
        return self.assignmentname   


class SubmitAssignment(models.Model):
    uploadid = models.AutoField(primary_key=True)
    assignmentid = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.SET_NULL,null = True)
    courseid = models.ForeignKey(Course, on_delete=models.SET_NULL,null = True)
    uploadurl = models.FileField(max_length=500,null = True,default='Not Uploaded yet',upload_to='images')
    createddate = models.DateTimeField(auto_now_add=True,null = True)
    
class StudentResult(models.Model):
    studentresultid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student,null =True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    totalmarks = models.IntegerField(null = True)
    marksobtained = models.IntegerField(null = True)
    classid = models.ForeignKey(TblClass,null = True,on_delete=models.DO_NOTHING)
    sectionid = models.ForeignKey(Section,null=True,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.studentid
    
class StudentAttendance(models.Model):
    studentattid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student,null =True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    totalclasses = models.IntegerField(null = True)
    classesattended = models.IntegerField(null = True)
    classid = models.ForeignKey(TblClass,null = True,on_delete=models.DO_NOTHING)
    
class Tests(models.Model):
    testid = models.AutoField(primary_key=True)
    teacherid = models.ForeignKey(schoolTeacher,null =True,on_delete=models.DO_NOTHING)
    testname = models.CharField(max_length = 20,null=True)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    classid = models.ForeignKey(TblClass,null = True,on_delete=models.DO_NOTHING)
    dayid = models.ForeignKey(Day,null = True,on_delete=models.DO_NOTHING)
    uploadurl = models.FileField(max_length=500,null = True,default='Not Uploaded yet',upload_to='images') 
    
    def __str__(self):
        return self.testname
    
class std_test(models.Model):
    std_testid = models.AutoField(primary_key=True)
    teacherid = models.ForeignKey(schoolTeacher,null =True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)

    
class ContactForm(models.Model):
    formid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null= True)
    email = models.EmailField(max_length=100, null= True)
    message = models.TextField(max_length=100, null= True)
    
    def __str__(self):
        return self.name
    
class StudentComplaint(models.Model):
    complaintid = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100, null= True)
    course_name = models.CharField(max_length=100, null= True)
    teachername = models.CharField(max_length=100, null= True)
    description = models.TextField(max_length=100, null =True)
    option = [('Good','Good'),('Average','Average'),('Poor','Poor')]
    rating = models.CharField(max_length=100, choices=option, default='none', null=True)
    submitdate = DateField(null = True)
    
    
    def __str__(self):
        return self.s_name
    