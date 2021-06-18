from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect

# Create your views here.

def index(request):
   if request.user.is_anonymous:
        #return render(request, 'login.html')
        return redirect('../')
   else:
         return render(request,'blog/index.html')
   
    