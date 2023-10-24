from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Form
from django.contrib.auth.models import User
from django.contrib import messages,auth


def main(request):
    return render(request,'index.html')
#login Page#
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user.save()
            return redirect('/reg')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

#reg part#
def reg(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dob=request.POST.get('dob',)
        age=request.POST.get('age',)
        gender=request.POST.get('gender',)
        phonenumber=request.POST.get('phonenumber',)
        mailid=request.POST.get('mailid')
        address=request.POST.get('address',)
        department=request.POST.get('department',)
        address=request.POST.get('address',)
        course=request.POST.get('course',)
        material=request.POST.get('material',)
        school=Form(name=name,dob=dob,age=age,gender=gender,phonenumber=phonenumber,mailid=mailid,address=address,department=department,course=course)
        school.save()
        return redirect('/login')
   
    return render(request,'reg.html')

#re 2nd part
def reg2(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        #password verification
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('/login')
              
            elif User.objects.filter(password=password).exists():
                messages.info(request,"password taken")
                return redirect('/login')
              
            else:
                myuser=User.objects.create_user(username=username,password=password)
                myuser.save()  
                return redirect('/login')
        else:
            messages.error(request,"password not match")
            return redirect("/reg2")
    return render(request,'reg2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
