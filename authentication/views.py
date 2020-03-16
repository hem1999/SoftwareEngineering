from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect 
from .models import Student , Professor , Project_user,   Project , Join_team
from django.db import connection
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, "authentication/home.html")

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender= request.POST.get('gender')
        acheivement = request.POST.get('acheivement')
        stream = request.POST.get('stream')
        contact_number = request.POST.get('contact_number')
        url = request.POST.get('url')
        sign_up_pswd = make_password(request.POST.get('password'))
        # sign_up = sign_up.save(commit = False)
        # sign_up.status = 1
        user = User(username = name ,password= sign_up_pswd)
        user.save()
        if(request.POST.get("person")=="professor"):
            obj = Professor(name= name , email = email , username= user , acheivements =acheivement, stream=stream , contact_number= contact_number , url=url)
            obj.save()
            return redirect('index')
        else:
            obj = Student(name= name , email = email , username= user , acheivements =acheivement, stream=stream , contact_number= contact_number , url=url)
            obj.save()
            return redirect('index')
    else:
        return render(request,"authentication/register.html")

def signin(request):
    if request.method=="POST":
        un= request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(request, username=un, password=pw)
        if  user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request,"authentication/login.html" ,{'msg': "wrong password/username"})
    else:
        return render(request , "authentication/login.html",{'msg': "." })

def dashboard(request , **kwargs):
    msg=""
    try:
        obj = Student.objects.get(name = request.user.username)
        return render(request , "authentication/dashboard.html" , {'accounttype':'student','user':obj , 'msg':msg} )
    except Student.DoesNotExist:
        obj = Professor.objects.get(name = request.user.username)
        return render(request , "authentication/dashboard.html" , {'accounttype':'professor','user':obj , 'msg': msg } )
    # else:
    #     return render(request , "dashboard.html" , {'accounttype':'student','user':obj} )

def edit(request):
    try:
        obj = Student.objects.get(name = request.user.username)
    except Student.DoesNotExist:
        obj = Professor.objects.get(name = request.user.username)
    
    if(request.method=="POST"):    
        obj.email=request.POST.get('email')
        obj.acheivements = request.POST.get('acheivements')
        obj.stream = request.POST.get('stream')
        obj.contact_number = request.POST.get('contact_number')
        # obj.url = request.POST.get('url')
        obj.save()
        return redirect('dashboard')
    else:
        return render(request,"authentication/dashboard.html" ,{'user':obj})

#display my projects
def view_projects(request):
    #if request.method == "POST":
    #prof = Professor.objects.filter(name = request.user.username)
    proj = Project_user.objects.filter(user_id = request.user )
    l=[]
    for i in range(0,len(proj)):
        pr=proj[i].project_id
        l.append(Project.objects.get(id = pr.id))
    return render(request,"authentication/view_proj.html" , {'proj' :l})
    

def add_projects(request):
    if request.method=="POST":
        user = request.user
        proj_name = request.POST.get('proj_name')
        proj_description = request.POST.get('proj_description')
        proj=Project(proj_name = proj_name , proj_description = proj_description)
        proj.save()
        #prof = Professor.objects.get(name = request.user.username)
        pu =Project_user(user_id =request.user , project_id = proj)
        pu.save()
        return redirect('view_projects')
        #return HttpResponse("HELLO")
    else:
        return render(request,"authentication/add_projects.html")

def requests(request):
    if request.method == "POST":
        # return HttpResponse(request.POST.get('id'))
        id1 = request.POST.get('id')
        req = Join_team.objects.get(id =id1 )
        req.status = True
        req.save()
        # return HttpResponse("hello")
        return redirect('requests')

    else:
        user = request.user
        try:
            obj = Professor.objects.get(name = user.username )
        except:
            obj = Student.objects.get(name = request.user.username)

        req = Join_team.objects.filter(to_user = user.id , status= False )
        return render(request,"authentication/requests.html" ,{'req':req})
        

def join_team(request):
    if request.method =="POST":
        proj_id = request.POST.get('proj_id')
        proj = Project.objects.get(id = proj_id)
        user = request.user
        prof = Project_user.objects.get(project_id =proj)
        obj =Join_team(proj_id= proj_id , from_user = request.user , to_user = prof.user_id.id , status = False)
        obj.save()
        return render(request,"authentication/successfull.html")
    else:
        return HttpResponse("else")

def search_projects(request):
    #return HttpResponse("HELLO")
    if request.method=="POST":
        key_word = request.POST.get('proj_name')
        result = Project.objects.filter(proj_name__contains=key_word)
        return render(request,"authentication/display_projs.html" ,{'proj': result})
    else:
        return redirect('dashboard')


def status(request):
    return redirect('index') 

def logoutView(request):
    logout(request)
    return redirect('index')

def ratings(request):
    return redirect('index')