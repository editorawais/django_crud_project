import email
from re import U
from django import forms
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# Below function will show and add the user to database.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    zti = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': zti})

# Below function will delete.

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# Below function will Edit/Update.

def update_data(request, id):
    if request.method == 'POST':
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=ud)
        if fm.is_valid:
            fm.save()
    else:
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(instance=ud)
    return render(request, 'enroll/updatestudent.html', {'form' : fm})
        