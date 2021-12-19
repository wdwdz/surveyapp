from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    return render(request,'todo/home.html')

def about(request):
    return render(request,'todo/about.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html',{'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')


            except IntegrityError:
                return render(request, 'todo/signupuser.html',{'form':  UserCreationForm(), 'error': 'User name is taken'})
        else:
            return render(request, 'todo/signupuser.html',{'form': UserCreationForm(), 'error': 'Passwords not match'})
            # password not match

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',{'form': AuthenticationForm(), 'error': 'Username and password do not match'})
        else:
            login(request, user)
            return redirect('currenttodos')



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def createtodos(request):

    if request.method == 'GET':
        return render(request, 'todo/createtodos.html',{'form': TodoForm()})
    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('currenttodos')

def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, created__isnull=False)
    count = 3 - len(todos)
    return render(request, 'todo/currenttodos.html',{'todos': todos, 'count': count})


