from os import name
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group
from .models import *



# Create your views here.
def home(request):
    return render(request,'main.html')


def register(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name = 'student')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)          
            return redirect('loginPage')
                        
    context = {'form':form}
    return render(request, 'registration.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return render(request, 'login.html')

def about(request):
    return render(request, 'page2.html')

def contact(request):
    if request.method == "POST":
        contact = ContactForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = msg
        contact.save()
        messages.success(request, 'Thanks for contacting us! Your message was sent to the admin.')

    return render(request, 'contact.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def userpage(request):
    return render(request, 'dashboard.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def account_settings(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            
            
    context = {'form':form}
    return render(request, 'account_settings.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def assignments(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
                        
    assignments = Assignment.objects.all()   
    return render(request,'assig.html', {'assignments':assignments})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def complaint(request):
    student = request.user.student
    if request.method == "POST":
        complaint = StudentComplaint()
        s_name = request.POST.get('s_name')
        course_name = request.POST.get('course_name')
        teachername = request.POST.get('teachername')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        submitdate = request.POST.get('submitdate')
        complaint.s_name = s_name
        complaint.course_name = course_name
        complaint.teachername = teachername        
        complaint.description = description
        complaint.rating = rating        
        complaint.save()
    obj = StudentComplaint.objects.all() 
    return render(request, 'cff.html', {'obj':obj} )


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def timetable(request):
    
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            
    timetable = TimeTable.objects.all()
    return render(request,'schedule.html', {'timetable':timetable})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def result(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            
    result = StudentResult.objects.all()   

    return render(request,'studresult.html', {'result':result})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def std_att(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            
    std_att = StudentAttendance.objects.all()
    return render(request,'studattendence.html', {'std_att':std_att})

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def std_tests(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
    test = Tests.objects.all()
    return render(request,'tests.html', {'test':test})