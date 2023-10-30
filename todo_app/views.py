from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo_app import models
from todo_app.models import Todo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request,'signup.html')


def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/login')            
    return render(request,'signup.html')

def user_login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request,'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Todo(title=title, user=request.user)
        obj.save()
        user=request.user
        res=models.Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todo',{'res':res}) 
    res=models.Todo.objects.filter(user=request.user).order_by('-date') 
    return render(request, 'todo.html',{'res':res})

@login_required(login_url='/login') 
def e_todo(request,srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Todo.objects.get(srno=srno)
        obj.title=title
        obj.save()
        return redirect('/todo')
    
    obj = models.Todo.objects.get(srno=srno)
    return render(request, 'todo.html',{'obj':obj})

def del_todo(request,srno):
    print(srno)
    obj=models.Todo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')

def signout(request):
    logout(request)
    return redirect('/login')



