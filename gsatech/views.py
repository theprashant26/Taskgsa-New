from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *

def home(request):
    return render(request, 'index.html')

def profile(request):
    taskrecord = Task.objects.all()
    return render(request, 'profile.html',{'taskrecord':taskrecord})

class RegistrationformView(View):
    def get(self, request):
        form = RegistraionForm()
        return render(request, 'register.html', {'form':form})
    def post(self, request):
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            
def taskform(request):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        task_date = request.POST.get('task_date')
        task_time = request.POST.get('task_time')
        assigned_by = request.POST.get('assigned_by')
        task_status = request.POST.get('task_status')
        tform = Task.objects.create(taskname=taskname, task_date=task_date,task_time=task_time,assigned_by=assigned_by,task_status=task_status)
        tform.save()
        return redirect('/profile/')
        