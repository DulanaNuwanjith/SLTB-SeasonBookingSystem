from django.shortcuts import render
from app.models import Student, Season , Principal
from django.views.generic.edit import CreateView 
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.conf import settings
import os

class StudentCreateView (CreateView):
    template_name_suffix="_create"
    model=Student
    fields="__all__"
    success_url="studentlistview"

class StudentListView (ListView):
    template_name_suffix="_index"
    model=Student

class StudentDetailView (DetailView):
    template_name_suffix="_show" 
    model=Student

class SeasonCreateView (CreateView):
    template_name_suffix="_create"
    model=Season
    fields="__all__"
    success_url="seasonlistview"

class SeasonListView (ListView):
    template_name_suffix="_index"
    model=Season

class SeasonDetailView (DetailView):
    template_name_suffix="_show" 
    model=Season

class PrincipalCreateView (CreateView):
    template_name_suffix="_create"
    model=Principal
    fields="__all__"
    success_url="seasonlistview"

class PrincipalListView (ListView):
    template_name_suffix="_index"
    model=Principal

def About(request):
    render(request, "templates/app/about.html")

def Contact(request):
    render(request, "templates/app/contact.html")

def Service(request):
    render(request, "templates/app/service.html")