from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

#admin 1234
#mohit1 donbhai@1
def index(request):
   if request.user.is_anonymous:
       # return render(request, 'login.html')
       return redirect('../')
   else:
         return render(request,'index.html')
   
def loginuser(request):
     
     if   request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("../index")
             # A backend authenticated the credentials
        else:
        
             # No backend authenticated the credentials
             return render(request, 'login.html')
     else:
         return render(request, 'login.html')
          



def logoutuser(request):
    
        
        logout(request)
        return redirect('../')