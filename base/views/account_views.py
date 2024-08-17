from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from base.models import Item
from django.contrib.auth import authenticate,login,logout  ##



def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'pages/signup_login.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user=User.objects.create_user(username2,'',password2)
            return redirect('/login/')
    return render(request,'pages/signup_login.html',{'some':100})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user=authenticate(username= username2,password=password2)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signup/',{'error':'登録されていません'})
            
        
    return render(request,'pages/signup_login.html',{'some':100})