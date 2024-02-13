from django.http import HttpResponse
from django.shortcuts import render, redirect
from logpage.models import User_log
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    return render (request, 'index.html')

def signin(request):
    
    if request.method == "POST":
        fname = request.POST["username"]
        password = request.POST["pass1"] 
        try:
            obj = User_log.objects.get(first_name = fname)
        except:
            return HttpResponse("User not found")
        if check_password(password, obj.pass1):
            return HttpResponse ("Login")      
            
        else:
            return HttpResponse("Password wrong")
          
    return render(request,"signin.html")


def signup(request):
    if request.method =="POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if pass1 != pass2:
            messages.info(request,"Please use both password correct")
            return redirect('signup')
        
        else:
            data = User_log(first_name = fname, last_name = lname, email = email, pass1 = make_password(pass1))
            data.save()
            messages.info(request,"User created")
            return redirect('signin')
        
    return render (request, 'signup.html')

def signout(request):
    pass