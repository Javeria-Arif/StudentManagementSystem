from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name = 'home'),
path("navbar/", views.home, name = 'home'),
path("login/", views.loginPage, name = 'loginPage'),
path("logout/", views.logoutUser, name = 'logout'),
path("register/", views.register, name = 'register'),
path("about/", views.about, name = 'about'),
path("contact", views.contact, name = 'contact'),
path("userpage/", views.userpage, name = 'userpage'),
path("account_settings/", views.account_settings, name = 'account_settings'),
path("userpage/assignments/", views.assignments, name = 'assignments'),
path("complaint", views.complaint, name = 'complaint'),
path("schedule/", views.timetable, name = 'timetable'),
path("result/", views.result, name = 'result'),
path("attendance/", views.std_att, name = 'std_att'),
path("tests/", views.std_tests, name = 'std_tests'),
path("assignments/", views.assignments, name = 'assignments'),

]