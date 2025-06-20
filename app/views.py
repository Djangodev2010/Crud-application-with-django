from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'index.html', {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Invalid Credentials!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
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

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = True
    task.save()
    return redirect('/')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})
