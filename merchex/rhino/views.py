
from django.shortcuts import render


# Create your views here.
def app_rhino(request):
    return render(request, 'rhino/index.html')

def app_about(request):
    return render(request, 'rhino/about.html')

def app_contact(request):
    return render(request, 'rhino/contact.html')

def app_project(request):
    return render(request, 'rhino/project.html')

def app_staff(request):
    return render(request, 'rhino/staff.html')