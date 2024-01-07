from django.shortcuts import render
from django.shortcuts import HttpResponse
from home import models
# Create your views here.

def index(request):
    # return HttpResponse('This is index')
    
    return render(request, 'index.html') 

def about(request):
    # return HttpResponse('This is about')
    
    return render(request,'about.html') # passing context to about.html

def contact(request):
    # return HttpResponse('This is contact')
    #gathering the entered data into variables...
    if (request.method=="POST"):
        email = request. POST['email']
        name = request. POST['name']
        phone = request. POST['phone']
        gender = request. POST['gender']
        desc = request. POST['desc']

        ins = models.Contact(name=name, email=email, phone=phone, gender=gender, desc=desc)

        ins.save()
        print("\nData stored in the database succesfully!")
    return render(request,'contact.html')

def test(request):
    #context is a dictionary variable
    context = {
        'name':"suraj",
        'course':"Django"
    }
    return render(request,'test.html',context)