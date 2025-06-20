from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
            
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
