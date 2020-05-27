from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hello There... I am Ravi </h1>")

    return render(request, 'generator/home.html', {'password':'kjsdf0s990ij09SSE'})

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10
    thepassword=''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html',{'password':thepassword})
